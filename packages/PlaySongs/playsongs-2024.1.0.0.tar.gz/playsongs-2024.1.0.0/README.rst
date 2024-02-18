=============
**playsongs**
=============

Overview
--------

Play MP3s from a specified directory.

Prerequisites
-------------

- *Python >= 3.6*
- *playsound >= 1.2.2* (installed as a dependency)
- *pyobjc >= 7.1* (installed as a dependency)
- **CAVEAT**: Due to *playsound* limitations, directory and filenames with spaces are not allowed.

Required (Positional) Arguments
-------------------------------

- Position 1: /path/to/mp3/files

Optional (Keyword) Arguments
----------------------------

- repeat
    - Description: Number of times to repeat the whole collection.
    - Type: Integer
    - Default: 0
- shuffle
    - Description: Select whether to shuffle the list of songs being played.
    - Type: Boolean
    - Default: False

Usage
-----

Installation:

.. code-block:: BASH

   pip3 install playsongs
   # or
   python3 -m pip install playsongs

In Python3:

.. code-block:: BASH

   from playsongs import PlaySongs
   PlaySongs('/home/username/Music', repeat = 10000000, shuffle = True)

In BASH:

.. code-block:: BASH

   python3 -c "from playsongs import PlaySongs; PlaySongs('/home/username/Music', repeat = 10000000, shuffle = True)"
