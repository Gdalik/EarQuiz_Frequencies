![EarQuiz Frequencies Logo](/GUI/Icons/Logo/EarQuiz_Splash.png)

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/Gdalik/EarQuiz_Frequencies/blob/master/LICENSE)
[![Documentation](https://img.shields.io/badge/Documentation-on%20earquiz.org-brightgreen)](https://earquiz.org/manuals/earquiz-frequencies-help/)
[![Supported Platforms](https://img.shields.io/badge/platforms-macOS%20%7C%20Windows%20%7C%20Linux-yellow)]()

`EarQuiz Frequencies` is a software for technical ear training on equalization. Its main goal is to help musicians and all kinds of audio professionals or students (producers, recording/mixing/mastering/live sound engineers, audio designers, etc.) develop and master the ability to aurally recognize frequency bands. In general, anybody who wants to teach himself/herself how to adjust an audio system with equalizer by ear consciously may find it useful.

This application is based on the world-renowned [Golden Ears](https://goldenearsaudio.com/) method of David Moulton, whose course is half dedicated to building this essential critical listening skill. Built-in presets are similar to his easy-to-difficult patterns, but a user can also change the settings to do more than what is already available. This software may be used by educators in the audio industry to produce superb quality training and test materials for their students.

## Features

- Internal pink noise generator or any external audio file in WAV, AIFF, FLAC, or MP3 format as audio source.
- 15 built-in presets with increasing difficulty.
- 1-octave (10-band) and 1/3-octave (30-band) EQ.
- Exercise patterns with boost and/or cut frequencies.
- Single-band and Dual-band exercise patterns.
- Custom adjustable frequency gain level from ±1 to ±18 dB.
- Custom adjustable filter bandwidth/Q-factor.
- Auto peak-normalization, preventing digital clipping during equalization.
- Easy non-destructive trimming of external audio files.
- Adjustable example/slice length from 10 up to 30 seconds.
- Auto-saving trimmed ranges and example/slice lengths for different audio sources.
- Exporting learning and test audio file packages in WAV, AIFF, FLAC, MP3, or OGG format. 
- Audio format converter.
- Reading M3U, M3U8, PLS, XSPF playlists supported.
- Exporting M3U and M3U8 playlists supported.
- Convenient and flexible playlist navigation.
- Dark Mode support (on macOS, Linux, and Windows 11).
- And other features (see [EarQuiz Frequencies Help](https://earquiz.org/manuals/earquiz-frequencies-help/))...

## Installation

*To use the application out of the box, you can just download the distribution package for your OS (Windows or macOS), run it and follow the installation process.*

You can also clone (download) this repository and launch the program from [Python](https://www.python.org/). It has been tested with Python 3.9, 3.10 and 3.11.
So, make sure the proper version of interpreter is installed on your computer.

The repository doesn't contain any pre-compiled dependencies, so they should be installed before the application execution. Though it is technically possible to use the "base" Python environment,
[creating a separate virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment) for the project and all its packages is highly recommended. Then, once you have [activated the project's virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#activate-a-virtual-environment), installing all the requirements using the package manager is as simple as:

`pip install -r requirements.txt`

After that, you can start the application with:

`python -m main`

## Building from Source

You can build executables yourself for Windows, macOS or Linux from this codebase.

1. Use the platform you are going to build on. E.g., you cannot make an executable package for Windows under macOS, and creating a macOS bundle under Windows is not possible as well.
2. Make sure, the relevant version of Python is installed, a virtual environment for the project is created, all the requirements are installed,
and you can run the application from the source code, using the interpreter.
3. With the activated virtual environment, install [PyInstaller](https://pyinstaller.org/) using the package manager:<br /><br />
`pip install -U pyinstaller`<br /><br />
4. On macOS (Intel), run:<br /><br />
`pyinstaller macos_build.spec`<br /><br />
On macOS (Apple Silicon), run:<br /><br />
`pyinstaller macos_build-arm64.spec`<br /><br />
On Windows, run:<br /><br />
`pyinstaller windows_build.spec`<br /><br />
On Linux, run:<br /><br />
`pyinstaller linux_build.spec`<br /><br />

The bundled application should now be available in the *dist* folder.

## License

`EarQuiz Frequencies` is Copyright &copy; 2023-2024 by Gdaliy Garmiza.<br />
`EarQuiz Frequencies` is licensed under the [GNU General Public License v3](https://github.com/Gdalik/EarQuiz_Frequencies/blob/master/LICENSE).

This application uses the following open source libraries:
- [PyQt6](https://www.riverbankcomputing.com/software/pyqt/)<br />
Copyright &copy; 2021-2024 Riverbank Computing Limited<br />
License: [GPL v3](https://www.gnu.org/licenses/gpl-3.0.html)
- [Pedalboard](https://spotify.github.io/pedalboard/index.html#)<br />
Copyright &copy; 2021-2024 Spotify AB<br />
License: [GPL v3](https://www.gnu.org/licenses/gpl-3.0.html)
- [NumPy](https://numpy.org/)<br />
Copyright &copy; 2005-2024 NumPy Developers<br />
License: [BSD 3-Clause](https://opensource.org/license/bsd-3-clause/)
- [PyQtGraph](https://www.pyqtgraph.org/)<br />
Copyright &copy; 2012-2024 University of North Carolina at Chapel Hill<br />
License: [MIT](https://opensource.org/license/mit/)
- [tendo](https://pypi.org/project/tendo/)<br />
Copyright &copy; 2010-2022 Sorin Sbarnea<br />
License: [Python Software Foundation License](https://docs.python.org/3/license.html#psf-license)

## Privacy Policy
This program will not transfer any information to other networked systems unless specifically requested by the user or the person installing or operating it.

## Code Signing Policy
For Windows binaries, starting from version 0.1.5, this application uses free code signing provided by [SignPath.io](https://signpath.io/), and a certificate by the [SignPath Foundation](https://signpath.org/).
