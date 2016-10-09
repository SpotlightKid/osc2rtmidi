# -*- coding:utf-8 -*-
#
# rosc2rtmidi/elease.py - release information for the osc2rtmidi package
#
"""A configurable uni-directional OSC to MIDI gateway.

An extended example for usage of the python-rtmidi package.

.. _python-rtmidi: http://chrisarndt.de/projects/python-rtmidi

"""

name = 'osc2rtmidi'
version = '0.1'
description = __doc__.splitlines()
keywords = 'rtmidi, midi, music, OSC'
author = 'Christopher Arndt'
author_email = 'chris@chrisarndt.de'
url = 'https://github.com/SpotlightKid/%s.git' % name
repository = url
download_url = 'https://pypi.python.org/pypi/%s' % name
license = 'MIT License'
platforms = 'POSIX, Windows, MacOS X'
long_description = "\n".join(description[2:]) % locals()
description = description[0]
classifiers = """\
Development Status :: 4 - Beta
Environment :: MacOS X
Environment :: Win32 (MS Windows)
Environment :: Console
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: MacOS :: MacOS X
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Topic :: Multimedia :: Sound/Audio :: MIDI
Topic :: Software Development :: Libraries :: Python Modules
"""
classifiers = [c.strip() for c in classifiers.splitlines()
               if c.strip() and not c.startswith('#')]
try:  # Python 2.x
    del c  # noqa
except:
    pass
