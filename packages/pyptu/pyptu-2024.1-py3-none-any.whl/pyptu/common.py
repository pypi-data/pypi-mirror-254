#!/usr/bin/env python3

'''
Constants.
'''

import struct


def _invert_dict(dct):
    '''
    Invert a dict.
    '''
    return {value: key for (key, value) in dct.items()}


def set_attributes(obj, dct, prefix=''):
    '''
    Declare all key-value pairs in a dict as attributes of the given object.
    This is useful for declaring global variables in modules.

    Args:
        obj:
            The object on which to set the attributes.

        dct:
            A dict or other object with an "items()" method that returns
            key-value pairs. Each key will be made an attribute of obj with the
            associated value.

        prefix:
            An optional string to prefix to the key to create an attribute name.
    '''
    for key, value in dct.items():
        setattr(obj, f'{prefix}{key}', value)


def bitmask(size):
    '''
    Get a bitmask.

    Args:
        size:
            The number of bits in the bitmask.

    Returns:
        The bitmask.
    '''
    return (1 << size) - 1


TAG_NAME_TO_VALUE = {
    name: struct.unpack('>i', bytes.fromhex(value))[0]
    for (name, value) in (
        ('Empty8',      'FFFF0008'),
        ('Bool8',       '00000008'),
        ('Int8',        '10000008'),
        ('BitSet64',    '11000008'),
        ('Color8',      '12000008'),
        ('Float8',      '20000008'),
        ('TDateTime',   '21000008'),
        ('Float8Array', '2001FFFF'),
        ('AnsiString',  '4001FFFF'),
        ('WideString',  '4002FFFF'),
        ('BinaryBlob',  'FFFFFFFF')
    )
}

TAG_VALUE_TO_NAME = _invert_dict(TAG_NAME_TO_VALUE)

RECORD_NAME_TO_VALUE = {
    name: struct.unpack('>i', bytes.fromhex(value))[0]
    for (name, value) in (
        ('PicoHarpT3',     '00010303'),
        ('PicoHarpT2',     '00010203'),
        ('HydraHarpT3',    '00010304'),
        ('HydraHarpT2',    '00010204'),
        ('HydraHarp2T3',   '01010304'),
        ('HydraHarp2T2',   '01010204'),
        ('TimeHarp260NT3', '00010305'),
        ('TimeHarp260NT2', '00010205'),
        ('TimeHarp260PT3', '00010306'),
        ('TimeHarp260PT2', '00010206'),
        ('MultiHarpT3',    '00010307'),
        ('MultiHarpT2',    '00010207')
    )
}

RECORD_VALUE_TO_NAME = _invert_dict(RECORD_NAME_TO_VALUE)
