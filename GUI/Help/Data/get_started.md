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

<a id="the-basic-training-method">The overall training process involves ongoing learning and testing yourself</a>.
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
Therefore, if we have 10 seconds length example, this would be: 3sec **EQ Off**, 4sec **EQ On** and 
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
**Learn** mode button **or** change the position of any EQ sliders' handle by dragging/clicking on it, which will switch the application
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
<a id="setting-volume-level">The main idea for the volume</a> is to set the comfortable level for the whole Learn/Test exercise cycle with the same audio stuff
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
with in-app training we also run into a kind of compromise between sound quality, overall loudness and alignment of levels between 
exercises with different audio sources and settings.

As my priority is to achieve the best possible sound quality without clipping as a side effect of boosting frequencies,
I have decided to apply to every audio source of single-band exercise the preventive peak normalization with opposite number to current absolute value
of frequency gain.
For dual-band EQ patterns, I have added extra-headroom from 1 up to 3dB. 

So, there is an inverse relationship between equalization depth and peak normalization level (the more the frequency gain, 
the quieter the source before the equalization and vice-versa). 
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
(this will automatically set the relevant **Audio Source** mode and switch the application to the **Preview** mode as well; 
see details [here](#working-with-external-audio-files)).

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

### Equalization: Patterns, Sliders and Settings 

#### Equalization Patterns
**EQ Pattern** is a core of each exercise, as it defines:
- the range of frequency options;
- default **EQ Settings** (Frequency Gain and Bandwidth/Q factor of filters);
- the type of **Equalizer**: 1-octave (10-band) or 1/3-octave (30-band);
- if the frequencies would be boosted or cut, or both options;
- if one or two frequency bands would be treated at once;
- for dual-band presets: the minimal range between altered frequency bands.

There are 15 presets with increasing difficulty: from boosting a single 1-octave band within a limited frequency range (lows, mids, highs separately)
to boosting or cutting two 1/3-octave bands simultaneously in the full range. 
You can choose any pattern from the list or skip forward with the <span style="color:blue; font-weight:bold">></span> 
(**Next Equalization Pattern**) button. This can be made silently (without triggering other actions) in the **Preview** mode, 
unlike in the **Learn** or the **Test** modes, where it resets the exercises and their playback.

The current EQ pattern is stored between sessions.

#### Equalization Sliders
**EQ Sliders** are the main input controllers for the training (**Learn** and **Test**) modes. The numbers below each of them
represent the central frequencies of corresponding frequency bands. And the positions of sliders' handles determine the boost or cut
of particular bands, whether real or guessed.

However, in the **Learn**
mode one may need to manually trigger them only to force the boost/cut of specific frequencies in the following example,
since this is done automatically otherwise. In the **Test** mode a user enters his or her answers pushing the 
appropriate sliders' handles up or down.

The frequency range of the current EQ Pattern determines the range of available/enabled sliders when the app is ready for
the corresponding input. The 25Hz and the 20kHz sliders of the 30-Band EQ are permanently disabled, since these frequencies are 
at the boundaries of our perception and most systems' reproduction.

The initial positions of sliders' handles depend on the current EQ Pattern. If frequency bands are to be boosted, they are
at the bottom of the sliders. If frequency bands are to be cut, they are at the top of the sliders. When both options
are possible, the handles are at the vertical center.

With *single-band* patterns, the input is accepted when a user changes the position of a slider handle. There is no way to
change the mind within the example here.

With *dual-band* patterns, the input is accepted when the position of two sliders' handles
is changed. After a user has dragged or clicked on a first slider, one or more adjacent sliders are disabled.
This is because the option to simultaneously alter two frequency bands, that are too close to each other, is intentionally
avoided, as it would become a kind of "mind game" otherwise. While the user hasn't chosen a second slider, he or she can
return the first one to its initial state and reconsider the input.

#### Equalization Settings
You can open the **EQ Settings** by pressing the button with gear icon in the top-right corner
of the EQ or by selecting **View | EQ Settings** from the main menu.
They consist of two parameters: 
1. *Frequency Gain*, that determines an amount by which the center frequency of filter is boosted or cut.
2. *Bandwidth*/*Q factor*, that are used to set the width of boosted or cut frequency band.

Here is a filter scheme:

<br />

<img align="center" src=":/Getting_Started/Data/Images/BellFilterScheme.png"/>

This type of filter is called *peaking* or *bell* bandpass filter.
Center frequency (f<sub>0</sub>) which is determined by the choice of an EQ Slider, is the most altered (boosted or cut) 
point within a frequency band.
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

In general, the narrower/steeper filter curve, the more accurately and precisely it works.
The wider band, conversely, affects more frequencies and makes equalization more prominent, but less exact.
With too high Q factor, the situation,
when there is no audible content in particular part of spectrum, is more likely. With too low one, the boundaries
between frequency bands may become blurred.

For presets with 10-band EQ I have set the default bandwidth to 1 octave with ±12dB gain, and for those with 30-band EQ I have used
the 1/3-octave value with ±15dB gain.

You can set your custom options in the **Preview** mode or in the **Learn** mode between playback of examples. The app
will re-normalize your audio according to current Frequency Gain and EQ pattern. Pressing the **Reset** button restores 
default EQ pattern settings.

If you want to use the same settings across various EQ patterns, you can **Lock** them with the corresponding button.
For example, you have become confident with all the patterns, and you want to boost your proficiency. In this case,
while going through the same patterns, 
you can try lowering the frequency gain value, and challenge your ears to hear the subtler and subtler equalization.

When locked, this state and values themselves are stored between sessions.

### Working with External Audio Files

<a id="working-with-external-audio-files">There are</a> different ways to load external audio into the software:
- Select **File | Open Files...** from the main menu, or press **Ctrl+O** (on Windows) or 
**⌘O** (on macOS), or click on <span style="color:green; font-weight:bold">+</span> in the **Audio Source** window.
- Select **File | Open Folder...** from the main menu.
- Drag & Drop files to the **Playlist** from anywhere possible.

The methods above can be used both for locating audio files of [the supported formats](#supported-audio-formats) directly
or through playlists. Currently, parsing of M3U, M3U8, PLS and XSPF playlists is supported.

After adding audio files to the **Playlist**, you can load each of them in various ways.
If you haven't loaded any audio file before, in case you manually switch the **Audio Source** to the **Audio File (Playlist)** mode,
pressing the **Play** button or choosing **Controls | Play** from the main menu will load and start playing the first track.
However, with **Shuffle Playback** option checked, a random audio file will be chosen. 

You can also load any track you want just by double-clicking on it or by selecting it and pressing *Enter*. This will switch the **Audio Source** to the 
**Audio File (Playlist)** mode automatically.

For further playlist navigation, you can use the **Previous Track** / **Next Track** player controls or similar buttons above the **Playlist**. 
When you are not in the **Preview** mode, the player skip controls/buttons won't be available, though. In this case, if you want to go forward/backward
in the playlist, you can still use the buttons above the **Playlist**. This will switch the programme to the **Preview**
mode, whatever the current mode is. Any training process will be cancelled. Moreover, every change of an audio source resets the application to the **Preview** mode. 

On the first switch to **Audio File (Playlist)**, 
the **Transport Panel** becomes visible automatically. Here we may take the most advantage of the latter.

One of the main purposes of the **Preview** mode is to let a user select and **trim** an audio track region for further training. The white inside
gray zones of the audio timeline slider at the **Transport Panel** represent the trimmed region inside a whole audio track.
By default, each region starts at zero, and its length is equal to **Slice Length** (length of each future training example) multiplied by ten or by 
a smaller maximum number which can fit the length of a track. 

You can move left and right bounds of the region separately, and the whole region as well, by dragging the mouse cursor.
The start/end values can also be set with the corresponding spin boxes. Clicking on the <span style="color:blue; font-weight:bold">Start</span>
and the <span style="color:blue; font-weight:bold">End</span> buttons at the left sides of the spin boxes would set these values to
the current audio cursor position if possible, no matter if an audio file is playing or not. It may be pretty convenient to set the bounds
"on the fly" during the playback. The <span style="color:blue; font-weight:bold">[←</span> and the 
<span style="color:blue; font-weight:bold">→]</span> buttons at the right sides of the spin boxes can be used to set the starting
point to the beginning of a file, and to set the ending point to the end of a file, respectively.

The bounds' values of regions and the slice lengths are stored for each audio file on another file load or when the application
is about to be closed. When these audio files are loaded again (which is detected through hashing), these settings are restored.

Pressing the **Clear** button at the right of the start/end spin boxes resets the region bounds to default for newly loaded files, and
restores the previously saved values for already known ones.

The current **Playlist** and the latest audio source used are stored between sessions. However, I highly recommend 
saving the collections you would like to use repeatedly with **File | Export Playlist...** options.

***Useful Tip***

*Before doing training exercises in the **Learn** and the **Test** modes, prepare your own collection of trimmed audio files, 
using the above-described application tools. Then uncheck the **Controls | Start Playing After Loading Track in Preview Mode** 
option in the main menu if checked. Adjust the volume level for your EQ Pattern and EQ Settings (see details [here](#setting-volume-level)).
Load external audio files as audio source for your exercises without playing them in the **Preview** mode. This will help you to
leave the volume knobs untouched as long as possible, while navigating through different audio sources/tracks.*


--------
### Annotations
#### Pink Noise

<a id="pink-noise">Pink noise</a> is a kind of random noise which has equal energy in different octave ranges. It derives from white noise which
is a random signal with wide frequency range and equal power for each frequency. Since the number of frequencies in octave doubles
for each octave increase, the energy of white noise doubles in each higher octave as well, which is 3 dB/oct. boost. In other words, white noise
gives the *impression* of high-frequencies dominance.
In pink noise, the energy falls proportionally to frequency, which is 3 dB/oct. attenuation, starting from 1 Hz, applied to white noise. This gives much more flat/even result from
a human ear perspective, and the spectrum of pink noise is the closest one to average music signal.

[< Back to "The Basic Training Method"](#the-basic-training-method)

#### Supported Audio Formats
<a id="supported-audio-formats">The fully supported audio formats</a> are: WAVE, AIFF, MP3 and FLAC. The OGG format is half-supported.
OGG audio files can be added to the **Playlist**, but they cannot be played with the current media
player backend neither on Windows nor on macOS. If you try to load an OGG file, you will get the error message
with option to proceed with conversion to WAVE or AIFF. There is also a known backend issue with incorrect FLAC files'
playback position on macOS, which may occur when starting playing from non-zero position. To work around
these format problems, you can convert audio files to WAVE or AIFF beforehand by selecting them and choosing 
**File | Convert Selected Files...** from the main menu or the similar option from the right-click context menu of the **Playlist**.

[< Back to "The Basic Training Method"](#the-basic-training-method)<br />
[< Back to "Working with External Audio Files"](#working-with-external-audio-files)

#### Remembering Frequency Bands
#### <a id="remembering-frequencies">[Write text here...]</a>
You mentally connect the highlighted frequency numbers with certain pitches, 
make your own associations (both aural and non-aural/"synesthetic"), note and try to describe the changes in 
character/timbre of different sounds.
