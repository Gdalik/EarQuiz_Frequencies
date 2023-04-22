<img align="left" src=":/Logo/Icons/Logo/EarQuiz_Header.png"/>

## EarQuiz Frequencies  
### &copy; 2023 Gdaliy Garmiza. [https://www.earquiz.org](https://www.earquiz.org)

----------------

### Greetings!

*EarQuiz Frequencies* is a software for technical ear training. It aims to help musicians 
and all kinds of audio professionals or students (producers, recording/mixing/mastering/live sound engineers, 
audio designers, etc.) develop and master the ability to aurally recognize frequency bands. In fact, anybody 
who wants to teach himself/herself how to adjust an audio system with equalizer by ear consciously may find it useful.

This application is based on (and deeply inspired by) the world-renowned *[Golden Ears](https://goldenearsaudio.com/)* method of David Moulton, 
whose course is half dedicated to building this essential critical listening skill. The pre-built presets generally 
follow his easy-to-difficult patterns, but you can also adjust the settings to go far beyond their boundaries.
Educators in the audio industry may use this software to produce superb quality training and test materials for their students 
almost in no time.

The programme is distributed under [GNU GPL v3 License](https://www.gnu.org/licenses/gpl-3.0.html). So, it is Free for any use, 
either personal or commercial!

<br />

### The Basic Training Method

<a id="the-basic-exercise-principle">The overall training process involves ongoing learning and testing yourself</a>.
Both learning and test exercises consist of audio samples, which we will call *examples*. Each example is a 10-30 
seconds' long chunk of either **[pink noise](#pink-noise)** (generated on each application launch) or **music**.  
Technically, any external audio file of a [supported format](#supported-audio-formats), stored locally on your device, can be used instead for the latter.
So, you could further experiment with recordings of speech, different sounds, natural or synthetic noises, 
whatever you have in your audio collection.

The method behind every example is fairly simple. It begins normally, with no spectral changes. After several seconds, 
the octave or 1/3-octave graphic equalizer (EQ) which boosts or cuts the amplitude of one or two frequency bands, is switched on 
automatically. After some more seconds, the EQ is switched off again, and the sound is returned to its normal 
(non-equalized) state.

<br />
<br />

<img align="center" src=":/Getting_Started/Data/Images/Drill_structure.png"/>

*Note: The current proportion of equalized part length versus sum length of non-equalized ones is hard-coded at 40/60 per cent.
Therefore, if we have 10 seconds length example, this would be: 3sec **EQ Off**, 4sec **EQ On**, and 
3sec **EQ Off** respectively.
The option to adjust this setting is planned to be introduced in future versions.*

Regardless of the audio source material and the EQ settings, the recommended approach remains the same.
- First, you **learn** and warm-up by listening to examples, trying to [memorize and internalize](#remembering-frequencies) 
the sound of different frequency ranges. <br /> *Don't be scared; just relax, listen, watch the
highlighted frequency values on the screen, and let your brains do the job ;-)!*
- Second, you take a **test** which is nothing but a sequence of ten similar examples with randomly chosen frequency values 
and boost/cut options (where available), which you guess, and get a score to track your progress.

<br />

### Choosing Acoustic Device
If you can do these exercises in a well treated room with studio quality monitors, it is great, 
but not obligatory. Decent consumer systems that do not add obvious distortion, crackling noises, etc. to sound 
at tolerably loud levels, and reproduce a wide frequency range 
([see further](#checking-frequency-range) about checking this), can also meet our requirements. 

You can use quality headphones as well. It is much easier and cheaper to achieve the accurate sound with them, 
one of the main reasons being that it is not affected by the room acoustics. Be aware, though, that pitch and loudness 
perception in headphones may significantly differ from the experience with loudspeakers. And you cannot feel the sound 
with your whole body this way, which may be especially important for analysing the lower end of the spectrum.
<br />

### Checking Audio Playback

Obvious, but important: make sure your audio system is switched on, and the playback audio path is working properly.
By default, the programme uses your system sound output device. But you can easily switch to any available 
audio playback device, selecting **Audio | Audio Device** menu item from the main menu.

Initially, the audio source is set to **Pink noise** so that the software would not require any external files to 
get up and running. And it is usually the best starting point for your practice session. So, make sure the corresponding
option is selected in the **Audio Source** window.

Are you ready to hear the sound :-)? Just press the 
**Learn** mode button **or** change the position of any EQ slider by dragging/clicking on it, which will switch the application
to the *Learn* mode automatically. After some processing (peak normalization and equalization) and loading, which usually takes fractions of second
on contemporary machines, the playback of an example should start.

*Here, you may want to proceed with the training process. But I suggest that we should **adjust your
audio system** first.* <br />

### Adjusting Audio System
The flatter, the better. I mean frequency response of your whole playback system, of course.
If your audio path contains any tone controls, equalizers, or sound processors, which affect the spectrum of reproduced sound,
in most cases, they should be switched off or set flat, unless you know for sure that they compensate for the certain flaws. If you have the 
loudness compensation button on your playback preamp or receiver, it should be off as well.
<br/>

#### Setting Volume Level
The main idea for the volume is to set the comfortable level for the whole Learn/Test exercise cycle with the same audio stuff
and EQ pattern, without changing the loudness during or between separate examples. Please note that our frequency 
perception is heavily influenced by the sound level (for more details, see studies by Fletcher and Munson on this topic).
So, at this stage, it makes sense to adjust the volume to a comfortable medium loud level while you check the audio playback 
using pink noise and current EQ pattern. You may need to reconsider it later for different EQ patterns/settings or other audio sources.

There is a **Volume Slider** with the level indicator both in percents (slider value) and decibels (relative amplitude level), 
which can be accessed from the **Transport Panel**. The latter can be opened from various places, including the top-right corner 
of the **Audio Source** window and **View** menu of the main menu.

It would be ideal to calibrate the audio system once, and not to touch the volume levels during the whole training session since then.
There is no big problem with this when exercises are packaged into a finished and mastered audio product, like a complete CD.
Software lets us gain from flexibility and the possibility to create exercises with very different settings from any audio material on the fly. However, 
with in-app training we also run into a kind of compromise between sound quality, overall loudness, and alignment of levels between 
exercises with different audio sources and settings.

As my priority is to achieve the best possible sound quality without clipping as a side effect of boosting frequencies,
I have decided to apply to every audio source of single-band exercise the preventive peak normalization with opposite number to current absolute value
of frequency gain.
For dual-band EQ patterns, I have added extra-headroom from 1 up to 3dB. 

So, there is an inverse relationship between equalization depth and peak normalization level (the more the frequency gain, 
the quieter the source before the equalization, and vice-versa). 
The former can be set from ±1 to ±18 dB, whereas the latter can vary from -1 to -21 dB. Both values are displayed at the status bar
at the right-bottom side of the main window, which may be helpful when adjusting the volume level under different settings.

Please, also keep in mind that when listening to external audio files in the **Preview** mode, the tracks are played back as they are, 
without any preventive normalization applied.
As a result, commercially mastered and other tracks with maximized levels may sound too loud compared to the same tracks in the training 
(**Learn** and **Test**) modes. So, it is usually worth reducing the volume approximately by the absolute value of frequency gain 
before you switch from the training modes back to the **Preview** mode. For more convenient restoring of the
**Volume Slider** value for training, you may use the **Save Volume Level** and **Restore Volume Level** features, available from the **Volume Slider** 
right-click context menu or from the **Audio** menu of the main menu.

Considering all above-mentioned, I should acknowledge that I am still in search for the optimal and technically efficient
solution here, which would provide the best user experience without sacrificing quality.
<br />

#### Quick Checking Frequency Range and Response
<a id="checking-frequency-range">To check out</a> if your playback system reproduces the wide enough frequency range for our exercises, we will need
the special calibration test audio file. To generate it, simply select **File | Make and Open Calibration Sine Waves File**
from the main menu. After having been created, the file "1kHz__10kHz__100Hz__15kHz__40Hz Sinus Tones.wav" will be added
to the **Playlist** and selected. To load it, you can just double-click on it or press the *Enter* key without changing the selection
(this will automatically set the relevant **Audio Source** mode, and switch the application to the **Preview** mode as well).

The name of the file exactly reflects its content. There are five sinus tones with different frequencies, lasting 5 seconds
each, and separated with 1 second of silence from each other. All the tones have the equal amplitude, which is 20% of the highest
possible (approximately -14dB).

Here is the timeline table, to make it even clearer and easier to use:

<br />

| Frequency | Time (sec)  |
|:----------|:------------|
| 1 kHz     | 1&mdash;6   |
 | 10 kHz    | 7&mdash;12  |
| 100 Hz    | 13&mdash;18 |
| 15 kHz    | 19&mdash;24 |
| 40 Hz     | 25&mdash;30 |

<br />

You should be able to hear the first three tones (1 kHz, 10 kHz and 100 Hz) clearly. If they vary in loudness, it is not a problem
unless this difference is too big. If you cannot hear one or more of these, you have a serious issue with your playback system, which
must be resolved before going on. In case only the last two tones (15 kHz and 40 Hz) are barely audible or even inaudible, you can
proceed, but be aware that you may have difficulties hearing/identifying the low or the high extremes of the spectrum correspondingly. 

### Equalization: Patterns, Settings and Sliders 

#### Equalization Patterns
**Equalization Pattern** is the core of each exercise, as it defines:
- the range of frequency options;
- default **EQ Settings** (Frequency Gain and Bandwidth/Q factor of filters);
- the type of **Equalizer**: 1-octave (10-band) or 1/3-octave (30-band);
- if the frequencies would be boosted or cut, or both options;
- if one or two frequency bands would be treated at once;
- for dual-band presets: the minimal range between altered frequency bands.

There are 15 presets with increasing difficulty: from boosting a single 1-octave band within a limited frequency range (lows, mids, highs separately)
to boosting or cutting two 1/3-octave bands simultaneously in the full range. 
You can choose any pattern from the list or skip forward with the <span style="color:blue; font-weight:bold"> > </span> 
(**Next Equalization Pattern**) button. This can be made silently (without triggering other actions) in the **Preview** mode, 
unlike in the **Learn** or the **Test** modes, where it resets the exercises and their playback.

#### Equalization Settings
**EQ Settings** consist of two parameters: 
1. *Frequency Gain*, that determines an amount by which the center frequency of filter is boosted or cut.
2. *Bandwidth*/*Q factor*, that are used to set the width of boosted or cut frequency band.

Here is a filter scheme:

<br />

<img align="center" src=":/Getting_Started/Data/Images/BellFilterScheme.png"/>

This type of filter is called *peaking* or *bell* bandpass filter.
Center frequency (f<sub>0</sub>) is the most altered (boosted or cut) point within a frequency band.
To measure how wide or narrow the whole band is, we need two symmetrical points on the left (f<sub>1</sub>) and 
on the right (f<sub>2</sub>) side of this peak, which have the 3dB roll-off (50% drop in power/energy).

The absolute bandwidth (BW) in Hz is simply the difference between the highest and the lowest frequencies:

<br />
<br />
<img src=":/Formulas/Data/Images/BW_form.png"/>
<br />

But our perception is not linear. The same music intervals will contain different number of Hz in different spectral ranges.
An absolute difference in Hz doubles with each increase of 1 octave.
That is to say, there is an octave between 50 and 100 Hz, 100 and 200 Hz, 200 and 400 Hz, 400 and 800 Hz, etc.
So, for our ears, the *ratio* between frequencies (f<sub>2</sub>/f<sub>1</sub>) matters much more than their absolute difference. 
This is why bandwidth of filters is also measured in octaves.

To calculate the difference in octaves between f<sub>1</sub> and f<sub>2</sub>, means to detect how many times we should multiply
f<sub>1</sub> by 2 to get f<sub>2</sub>. If we translate this into algebraic expression, we get the following formula:

<br />
<br />
<img src=":/Formulas/Data/Images/BWoct_form.png"/>
<br />

In our case, we deal with 1-octave and narrower bands, that's why we have BW values between 0 and 1.

Even more often than BW, we encounter the *Q factor* (abbrev. from *Quality factor*) as a filter parameter. Though used interchangeably often, 
they are not the same. In fact, they have inverse correlation: the bigger the Q, the narrower the band; the wider the band, 
the smaller the Q. If we know the absolute BW in Hz and the center frequency of a filter, the Q is easily calculated:

<br />
<br />
<img src=":/Formulas/Data/Images/Q_from_BW_form1.png"/>
<br />

But as we mostly deal with relative BW in octaves, we might want to know, how to convert them to those weird Q numbers.
This formula is a bit more complicated:

<br />
<br />
<img src=":/Formulas/Data/Images/Q_from_BW_form2.png"/> <br />
where N is number of octaves.

Enough with algebra and formulas here. The one that converts Q factor to BW in octaves is rather big, by the way.

For *Bandwidth*, I have used the options which can easily be thought of as music (tempered-scale) intervals:
<br />

| Bandwidth | Q      | Interval |
|:----------|:-------|:---------|
 |1 Octave | ~1.41  | Octave   |
| 3/4 Octave| ~1.9   | Major 6th |
| 2/3 Octave| ~2.14  | Minor 6th |
| 1/2 Octave | ~2.87  | Tritone  |
| 1/3 Octave | ~4.32  | Major 3d |
| 1/4 Octave | ~5.76  | Minor 3d |
| 1/6 Octave | ~8.65  | Major 2nd |

--------
### Annotations
#### Pink Noise
#### <a id="pink-noise">[Write text here...]</a>
#### Supported Audio Formats
#### <a id="supported-audio-formats">[Write text here...]</a>
#### Remembering Frequency Bands
#### <a id="remembering-frequencies">[Write text here...]</a>
You mentally connect the highlighted frequency numbers with certain pitches, 
make your own associations (both aural and non-aural/"synesthetic"), note and try to describe the changes in 
character/timbre of different sounds.

[< Go Back](#the-basic-exercise-principle)