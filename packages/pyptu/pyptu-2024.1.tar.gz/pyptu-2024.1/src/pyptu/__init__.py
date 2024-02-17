#!/usr/bin/env python3

'''
PTU file parser.
'''

import logging
import pathlib
import struct
import sys
import time

import numpy as np
import pandas as pd

from pyptu.common import (
    RECORD_VALUE_TO_NAME,
    TAG_NAME_TO_VALUE,
    bitmask,
    set_attributes
)


LOGGER = logging.getLogger(__name__)
ENCODING = 'utf-8'

# Declare the tag names as global variables.
_THIS_MODULE = sys.modules[__name__]
set_attributes(_THIS_MODULE, TAG_NAME_TO_VALUE, prefix='TAG_')


class PTUParser():
    '''
    PTU file parser.

    Attributes:
        header:
            A dict mapping header fields to their values, or None if the file
            has not yet been loaded.

        photons:
            A Pandas dataframe with the loaded photon records, or None.

        markers:
            A Pandas dataframe with the loaded marker records, or None.

        overflows:
            A Pandas dataframe with the loaded overflow records, or None.
    '''

    def __init__(self, path, encoding=ENCODING):
        '''
        Args:
            path:
                A path to a PTU file. It will be loaded when
                :py:meth:`ptu.PTUParser.load` is called.

            encoding:
                The input file encoding (e.g. "UTF-8").
        '''
        self.path = pathlib.Path(path).resolve()
        self.encoding = encoding
        self.handle = None
        self.tag_version = None

        self.header = {}
        self.photons = None
        self.markers = None
        self.overflows = None

    def safe_read(self, size):
        '''
        Ensure that the expected number of bytes are read from the open file handle.

        Args:
            size:
                The number of bytes to read.

        Returns:
            The read bytes.

        Raises:
            EOFError:
                The file ended before the number of requested bytes could be read.
        '''
        buf = self.handle.read(size)
        if len(buf) != size:
            raise EOFError(
                f'Failed to read {size:d} byte{"s" if size > 1 else ""} '
                f'from {self.handle.name}'
            )
        return buf

    def _unpack(self, fmt, size):
        '''
        Unpack a value.

        Args:
            fmt:
                A format character recognized by struct.unpack. The
                little-endian character will be prepended.

            size:
                The number of bytes to unpack.

        Returns:
            The unpacked value. This assumes that a single value is to be
            unpacked and will therefore only return the first item.
        '''
        return struct.unpack(f'<{fmt}', self.safe_read(size))[0]

    def _read_int(self):
        '''
        Read an int from the file.
        '''
        return self._unpack('i', 4)

    def _read_long_long(self):
        '''
        Read a long long int from the file.
        '''
        return self._unpack('q', 8)

    def _read_double(self):
        '''
        Read a double from the file.
        '''
        return self._unpack('d', 8)

    def get_tag(self):
        '''
        Get the next header tag identifier, index and type.
        '''
        identifier = self.safe_read(32).strip(b'\0').decode(self.encoding)
        index = self._read_int()
        typ = self._read_int()
        return identifier, index, typ

    def parse_header(self):
        '''
        Parse the PTU file header.
        '''
        # All of the TAG_* constants are dynamically defined as global variables
        # when the module is loaded.
        #
        header = self.header
        while True:
            identifier, index, typ = self.get_tag()

            if index > -1:
                identifier = f'{identifier}({index})'

            # pylint: disable-next=undefined-variable
            if typ == TAG_Empty8:  # noqa: F821
                self.safe_read(8)
                header[identifier] = '<empty Tag>'

            # pylint: disable-next=undefined-variable
            elif typ == TAG_Bool8:  # noqa: F821
                header[identifier] = self._read_long_long() != 0

            elif typ in (
                # pylint: disable-next=undefined-variable
                TAG_Int8,  # noqa: F821
                # pylint: disable-next=undefined-variable
                TAG_BitSet64,  # noqa: F821
                # pylint: disable-next=undefined-variable
                TAG_Color8,  # noqa: F821
                # pylint: disable-next=undefined-variable
                TAG_Float8Array,  # noqa: F821
                # pylint: disable-next=undefined-variable
                TAG_BinaryBlob  # noqa: F821
            ):
                header[identifier] = self._read_long_long()

            # pylint: disable-next=undefined-variable
            elif typ == TAG_Float8:  # noqa: F821
                header[identifier] = self._read_double()

            # pylint: disable-next=undefined-variable
            elif typ == TAG_TDateTime:  # noqa: F821
                header[identifier] = time.gmtime(int((self._read_double() - 25569) * 86400))

            # pylint: disable-next=undefined-variable
            elif typ == TAG_AnsiString:  # noqa: F821
                header[identifier] = self.safe_read(
                    self._read_long_long()
                ).strip(b'\0').decode(self.encoding)

            # pylint: disable-next=undefined-variable
            elif typ == TAG_WideString:  # noqa: F821
                header[identifier] = self.safe_read(
                    self._read_long_long()
                ).strip(b'\0').decode('utf-16le', errors='ignore')

            else:
                raise ValueError(f'Unknown tag type: {typ}')

            if identifier == 'Header_End':
                break

    @property
    def record_type(self):
        '''
        The loaded record type.
        '''
        return self.header['TTResultFormat_TTTRRecType']

    @property
    def is_t2(self):
        'True if the record type contains T2 data.'
        record_type = self.record_type
        try:
            return RECORD_VALUE_TO_NAME[record_type].endswith('T2')
        except KeyError as err:
            raise ValueError(f'Unrecognized record type: {record_type}') from err

    @property
    def _global_resolution(self):
        '''
        The global resolution.
        '''
        return self.header['MeasDesc_GlobalResolution'] * (1e12 if self.is_t2 else 1e9)

    @property
    def number_of_records(self):
        '''
        The number of records.
        '''
        return self.header['TTResult_NumberOfRecords']

    def set_photons(self, rec_idx, time_tag, channel, dtime):
        '''
        Set the photon array. The array will be an n x 5 ndarray consisting of 5
        columns: record index, channel ID, time tag, resolved time tag, and
        dtime.

        Args:
            rec_idx:
                The record indices.

            time_tag:
                The calculated time tags.

            channel:
                The channel on which the photon was recorded.

            dtime:
                The dtime value of the photon.
        '''
        self.photons = pd.DataFrame({
            'Record Index': rec_idx,
            'Channel': channel,
            'Time Tag': time_tag,
            'Resolved Time Tag': time_tag * self._global_resolution,
            'Dtime': dtime
        })

    def set_markers(self, rec_idx, timetags, markers):
        '''
        Set markers.

        Args:
            rec_idx:
                The record indices.

            timetags:
                The marker timetags.

            markers:
                The marker values.
        '''
        self.markers = pd.DataFrame({
            'Record Index': rec_idx,
            'Time Tag': timetags,
            'Marker': markers
        })

    def set_overflows(self, rec_idx, overflows):
        '''
        Set overflows.

        Args:
            rec_idx:
                The record indices.

            overflows:
                The overflow values.
        '''
        self.overflows = pd.DataFrame({
            'Record Index': rec_idx,
            'Overflow': overflows
        })

    def _get_records(self):
        '''
        A generator over the records.
        '''
        num_records = self.number_of_records
        LOGGER.info(
            'Parsing %d record%s in %s',
            num_records,
            '' if num_records == 1 else 's',
            self.path
        )
        dtype = np.dtype('uint32')
        dtype.newbyteorder('<')
        uints = np.frombuffer(self.handle.read(), dtype=dtype)
        n_uints = uints.size
        if n_uints != num_records:
            LOGGER.error('Expected %d records but found %d', num_records, n_uints)
        return uints

    def _get_rec_idx(self, data):
        '''
        Get an array of record indices.
        '''
        return np.arange(data.shape[0], dtype=np.uint)

    def read_pt3(self):
        '''
        Parse PT3 records.
        '''
        # channel: 0:4
        # time: 4:16
        # nsync: 16:32
        data = self._get_records()
        channel = data >> 28
        dtime = (data >> 16) & bitmask(12)
        nsync = data & bitmask(16)

        rec_idx = self._get_rec_idx(data)
        ofl_correction = np.zeros_like(data)

        is_special = channel == 0xF
        is_photon = ~is_special
        is_special = np.flatnonzero(is_special)

        is_overflow = dtime[is_special] == 0
        self.set_overflows(
            rec_idx[is_special][is_overflow],
            1
        )
        ofl_correction[is_special[is_overflow]] = 0x10000
        ofl_correction = ofl_correction.cumsum()

        is_marker = ~is_overflow
        self.set_markers(
            rec_idx[is_special][is_marker],
            ofl_correction[is_special][is_marker] + nsync[is_special][is_marker],
            dtime[is_special][is_marker],
        )

        invalid_channel = np.logical_or(
            channel == 0,
            channel > 4
        )
        if invalid_channel.any():
            LOGGER.error(
                'Invalid channels detected: %s',
                sorted(set(channel[invalid_channel]))
            )

        self.set_photons(
            rec_idx[is_photon],
            ofl_correction[is_photon] + nsync[is_photon],
            channel[is_photon],
            dtime[is_photon]
        )

    def read_pt2(self):
        '''
        Parse PT2 records.
        '''
        ofl_correction = 0
        # channel: 0:4
        # dtime: 4:32
        # markers: 28:32
        data = self._get_records()
        channel = data >> 28
        dtime = data & bitmask(28)

        rec_idx = self._get_rec_idx(data)
        ofl_corrections = np.zeros_like(data)

        is_special = channel == 0xF
        is_photon = ~is_special
        is_special = np.flatnonzero(is_special)

        markers = data[is_special] & bitmask(4)
        is_overflow = markers == 0
        is_marker = ~is_overflow

        ofl_corrections[is_special[is_overflow]] = 0x0c8f0000
        ofl_correction = ofl_correction.cumsum()

        self.set_overflows(rec_idx[is_special][is_overflow], 1)

        is_marker = ~is_overflow
        self.set_markers(
            rec_idx[is_special][is_marker],
            ofl_correction[is_special][is_marker] + dtime[is_special][is_marker],
            markers[is_marker]
        )

        invalid_channel = channel > 4
        if invalid_channel.any():
            LOGGER.error(
                'Invalid channels detected: %s',
                sorted(set(channel[invalid_channel]))
            )

        self.set_photons(
            rec_idx[is_photon],
            ofl_corrections[is_photon] + dtime[is_photon],
            channel[is_photon],
            dtime[is_photon]
        )

    def read_ht3(self, version):
        '''
        Parse HT3 records.

        Args:
            version:
                The HT3 version.
        '''
        # special: 0:1
        # channel: 1:7
        # dtime: 7:22
        # nsync: 22:32
        data = self._get_records()
        channel = (data >> 25) & bitmask(6)
        dtime = (data >> 10) & bitmask(15)
        nsync = data & bitmask(10)

        rec_idx = self._get_rec_idx(data)
        ofl_correction = np.zeros_like(data)

        is_special = (data >> 31) == 1
        is_photon = ~is_special
        is_special = np.flatnonzero(is_special)

        is_overflow = channel[is_special] == 0x3F
        overflow_case_1 = np.logical_or(
            nsync[is_special][is_overflow] == 0,
            version == 1
        )
        overflow_case_2 = ~overflow_case_1
        ofl_correction[is_special[is_overflow]] = 0x400
        ofl_correction[is_special[is_overflow][overflow_case_2]] *= \
            nsync[is_special][is_overflow][overflow_case_2]

        self.set_overflows(rec_idx[is_special][is_overflow], 1)
        self.overflows.loc[overflow_case_2, ['Overflow']] = \
            nsync[is_special][is_overflow][overflow_case_2]
        ofl_correction = ofl_correction.cumsum()

        is_marker = np.logical_and(
            channel[is_special] >= 1,
            channel[is_special] <= 0xF
        )
        self.set_markers(
            rec_idx[is_special][is_marker],
            ofl_correction[is_special][is_marker] + nsync[is_special][is_marker],
            channel[is_special][is_marker]
        )

        self.set_photons(
            rec_idx[is_photon],
            ofl_correction[is_photon] + nsync[is_photon],
            channel[is_photon],
            dtime[is_photon]
        )

    def read_ht2(self, version):
        '''
        Parse HT2 records.

        Args:
            version:
                The HT2 version.
        '''
        # special: 0:1
        # channel: 1:7
        # timetag: 7:32
        data = self._get_records()
        channel = (data >> 25) & bitmask(6)
        timetag = data & bitmask(25)

        rec_idx = self._get_rec_idx(data)
        ofl_correction = np.zeros_like(data)

        is_special = (data >> 31) == 1
        is_photon = ~is_special
        is_special = np.flatnonzero(is_special)

        is_overflow = channel[is_special] == 0x3F
        self.set_overflows(rec_idx[is_special][is_overflow], 1)

        if version == 1:
            ofl_correction[is_special[is_overflow]] = 33552000
        else:
            overflow_timetag = timetag[is_special][is_overflow]
            timetag_is_not_zero = overflow_timetag != 0
            ofl_correction[is_special[is_overflow]] = 33554432
            self.overflows.loc[timetag_is_not_zero, ['Overflow']] = \
                overflow_timetag[timetag_is_not_zero]
            ofl_correction[is_special[is_overflow][timetag_is_not_zero]] *= \
                overflow_timetag[timetag_is_not_zero]

        ofl_correction = ofl_correction.cumsum()

        is_marker = np.logical_and(
            channel[is_special] >= 1,
            channel[is_special] <= 0xF
        )

        self.set_markers(
            rec_idx[is_special][is_marker],
            ofl_correction[is_special][is_marker] + timetag[is_special][is_marker],
            channel[is_special][is_marker]
        )

        photon_channel = channel[is_photon]
        channel_is_zero = photon_channel == 0
        self.set_photons(
            rec_idx[is_photon],
            ofl_correction[is_photon] + timetag[is_photon],
            np.where(channel_is_zero, 0, photon_channel + 1),
            0
        )

    @staticmethod
    def _log_count(msg, count):
        '''
        Log a count.

        Args:
            msg:
                A logging format string that accepts 2 positional arguments.

            count:
                The count to log.
        '''
        LOGGER.info(msg, count, '' if count == 1 else 's')

    def load(self):
        '''
        Load the configure file.

        Raises:
            EOFError:
                The file ended unexpectedly while trying to read bytes.

            ValueError:
                The file is not recognized as a PTU file or the record type is
                not supported.
        '''
        path = self.path
        encoding = self.encoding
        LOGGER.info(
            'Attempting to parse %s as a PTU file with %s encoding.',
            path,
            encoding
        )
        with path.open('rb') as handle:
            self.handle = handle

            if handle.read(8).strip(b'\0').decode(encoding) != 'PQTTTR':
                raise ValueError(f'{path} does not appear to be a PTU file')

            self.tag_version = self.safe_read(8).rstrip(b'\0').decode(encoding)
            LOGGER.debug('Tag version: %s', self.tag_version)

            self.parse_header()
            record_type = self.record_type
            try:
                record_name = RECORD_VALUE_TO_NAME[record_type]
            except KeyError as err:
                raise ValueError(f'Unrecognized record type found in {path}') from err

            LOGGER.info(
                '%s appears to contain record of type %s',
                path,
                RECORD_VALUE_TO_NAME[record_type]
            )

            if record_name == 'PicoHarpT2':
                self.read_pt2()

            elif record_name == 'PicoHarpT3':
                self.read_pt3()

            elif self.is_t2:
                self.read_ht2(1 if record_name == 'HydraHarpT2' else 2)

            else:
                self.read_ht3(1 if record_name == 'HydraHarpT3' else 2)

            self._log_count('Loaded %d photon record%s', self.photons.shape[0])
            self._log_count('Detected %d overflow%s', self.overflows.shape[0])
            self._log_count('Detected %d marker%s', self.markers.shape[0])
