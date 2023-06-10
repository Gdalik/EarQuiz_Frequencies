![EarQuiz Frequencies Logo](/GUI/Icons/Logo/EarQuiz_Splash.png)

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/Gdalik/EarQuiz_Frequencies/blob/master/LICENSE)
[![Documentation](https://img.shields.io/badge/Documentation-on%20earquiz.org-brightgreen)](https://earquiz.org/manuals/earquiz-frequencies-help/)
[![Supported Platforms](https://img.shields.io/badge/platforms-macOS%20%7C%20Windows-yellow)]()

`EarQuiz Frequencies` is a software for technical ear training on equalization. Its main goal is to help musicians and all kinds of audio professionals or students (producers, recording/mixing/mastering/live sound engineers, audio designers, etc.) develop and master the ability to aurally recognize frequency bands. In general, anybody who wants to teach himself/herself how to adjust an audio system with equalizer by ear consciously may find it useful.

This application is based on the world-renowned [Golden Ears](https://goldenearsaudio.com/) method of David Moulton, whose course is half dedicated to building this essential critical listening skill. Built-in presets are similar to his easy-to-difficult patterns, but a user can also change the settings to do more than what is already available. This software may be used by educators in the audio industry to produce superb quality training and test materials for their students.

## Features

- Internal pink noise generator or any external audio file in WAV, AIFF, FLAC or MP3 format as audio source.
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
- Exporting learning and test audio files packages in WAV, AIFF, FLAC, MP3, or OGG format. 
- Audio format converter.
- Reading M3U, M3U8, PLS, XSPF playlists supported.
- Exporting M3U and M3U8 playlists supported.
- Convenient and flexible playlist navigation.
- And other features (see [EarQuiz Frequencies Help](https://earquiz.org/manuals/earquiz-frequencies-help/))...

## Installation

*To use the application out of the box, you can just download the distribution package for your OS (Windows or macOS), run it and follow the installation process.*

You can also clone (download) this repository and launch the program from [Python](https://www.python.org/). It has been tested with Python 3.9 and Python 3.10.
So, make sure the proper version of interpreter is installed on your computer.

The repository doesn't contain any pre-compiled dependencies, so they should be installed before the application execution. Though it is technically possible to use the "base" Python environment,
[creating a separate virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment) for the project and all its packages is highly recommended. Then, once you have [activated the project's virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#activating-a-virtual-environment), installing all the requirements using the package manager is as simple as:

`pip install -r requirements.txt`

After that, you can start the application with:

`python -m main`

