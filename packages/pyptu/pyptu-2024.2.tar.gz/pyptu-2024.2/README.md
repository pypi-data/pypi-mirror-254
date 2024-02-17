---
title: README
author: Jan-Michael Rye
---

# Synopsis

Read [PicoQuant PTU files](https://github.com/PicoQuant/PicoQuant-Time-Tagged-File-Format-Demos). The code follows the same parsing logic as the [Python demo provided by PicoQuant](https://github.com/PicoQuant/PicoQuant-Time-Tagged-File-Format-Demos/blob/master/PTU/Python/Read_PTU.py) but is up to 40 times faster due to the use of vectorized operations using [Numpy](https://numpy.org/) arrays.

## Links

* [Homepage](https://gitlab.inria.fr/jrye/pyptu)
* [Repository](https://gitlab.inria.fr/jrye/pyptu.git)
* [Documentation](https://jrye.gitlabpages.inria.fr/pyptu)
* [Issues](https://gitlab.inria.fr/jrye/pyptu/-/issues)
* [PyPI Package](https://pypi.org/project/pyptu/)
* [Software Heritage](https://archive.softwareheritage.org/browse/origin/?origin_url=https%3A//gitlab.inria.fr/jrye/pyptu.git)

# Usage

## Python API

The data in the file is parsed into the following objects which are set as attributes of the parser:

* `headers` - A dict mapping header fields to their values.
* `markers` - A Pandas DataFrame where each row is a record index with an index, a time tag and a marker.
* `overflows` - A Pandas DataFrame where each row is a record with a record index and an overflow values.
* `photons.csv` - A Pandas DataFrame where each row is a record with a record index, a channel, a time tag, a resolved time tag (using the global resolution value), and a dtime value.


~~~python
from pyptu import PTUParser

# A path to a PTU file.
path = /tmp/example.ptu

# Instantiate the parser. If no encoding is specified, the parser will first
# attempt to load files using UTF-8 and then Windows-1252 encodings. Other
# encodings can be specified using the "encoding" argument.
parser = PTUParser(path)

# Example of passing the "encoding" argument to the initialization method.
# parser = PTUParser(path, encoding='utf-8')

# Load the data. The load method also accepts an "encoding" argument.
parser.load()

# Example of passing the "encoding" argument to the load method.
# parser.load(encoding='windows-1252')

# Once the file is loaded, the loaded data can be accessed via the following
# attributes.

# The PTU header data.
headers = parser.headers

# The Pandas DataFrame of photon data.
photons = parser.photons

# The Pandas DataFrame of marker data.
markers = parser.markers

# The Pandas DataFrame of overflow values.
overflows = parser.overflows

# The loaded data can also be saved to standard file formats with the "save"
# method. Call the method with the path to the desired output directory.
parser.save('output')
~~~

## Command-Line

The package installs the `pyptu` command-line tool that can be used to convert the data in a PTU file to JSON and CSV files. It accepts the path to a PTU file and an output directory.

~~~sh
# Extract the PTU data to files in an output directory.
pyptu example.ptu output_directory
~~~

The output directory will contain the following files:

* `header.json` - A JSON file with the headers described above.
* `markers.csv` - A CSV file containing the `markers` DataFrame.
* `overflows.csv` - A CSV file containing the `overflows` DataFrame.
* `photons.csv` - A CSV containing the `photons` DataFrame.

### Help Message

~~~
$ pyptu -h
usage: pyptu [-h] [--encoding ENCODING] path dir

Extract PTU data to standard files.

positional arguments:
  path                 A path to a PTU file.
  dir                  A path to an output directory.

options:
  -h, --help           show this help message and exit
  --encoding ENCODING  Specify the input filetype encoding. It must be an encoding type supported
                       by Python. If not given, the following encodings will be tried, in order:
                       utf-8, windows-1252.

~~~
