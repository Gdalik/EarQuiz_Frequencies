<img align="left" src=":/Logo/Icons/Logo/EarQuiz_Header.png"/>

## EarQuiz Frequencies  
### &copy; 2023 Gdaliy Garmiza. [https://earquiz.org/EQ_Frequencies/](https://earquiz.org/EQ_Frequencies/)

----------------

[Read Online Help >](https://earquiz.org/manuals/earquiz-frequencies-help/)
<img align='right' src=":/Getting_Started/Data/Images/EQ_Frequencies_Help_QRcode.png"/>

### Table of Contents

* [Greetings!](#greetings)
* [The Basic Training Method](#the-basic-training-method)
* [Short Start Guide](#short-start-guide)
* [Choosing Acoustic Device](#choosing-acoustic-device)
* [Checking Audio Playback](#checking-audio-playback)
* [Adjusting Audio System](#adjusting-audio-system)
    - [Setting Volume Level](#setting-volume-level)
    - [Quick Checking Frequency Range and Response](#checking-frequency-range)
* [Equalization: Patterns, Sliders and Settings](#eq-patterns)
    - [Equalization Patterns](#eq-patterns)
    - [Equalization Sliders](#equalization-sliders)
    - [Equalization Settings](#equalization-settings)
* [Working with External Audio Files](#working-with-external-audio-files)
* [The Learn Mode](#learn-mode)
* [The Test Mode](#test-mode)
* [How to Memorize Frequency Bands?](#memorizing-frequencies)
* [Annotations](#pink-noise)

<br />

### Greetings!

<a id="greetings">*EarQuiz Frequencies*</a> is a software for technical ear training. It aims to help musicians 
and all kinds of audio professionals or students (producers, recording/mixing/mastering/live sound engineers, 
audio designers, etc.) develop and master the ability to aurally recognize frequency bands. In fact, anybody 
who wants to teach himself/herself how to adjust an audio system with equalizer by ear consciously may find it useful.

This application is based on (and deeply inspired by) the world-renowned *[Golden Ears](https://goldenearsaudio.com/)* method of David Moulton, 
whose course is half dedicated to building this essential critical listening skill. The pre-built presets generally 
follow his easy-to-difficult patterns, but you can also adjust the settings to go far beyond their boundaries.
Educators in the audio industry may use this software to [produce superb quality training and test materials](https://earquiz.org/manuals/earquiz-frequencies-help/making-training-audio/) for their students 
almost in no time.

The program is [Free Software](https://www.gnu.org/philosophy/free-sw.html), distributed under [GNU GPL v3 License](https://www.gnu.org/licenses/gpl-3.0.html). 
It is free for any use, either personal or commercial!

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
- First, you **learn** and warm-up by listening to examples, trying to [memorize and internalize](#memorizing-frequencies) 
the sound of different frequency ranges. <br /> *Don't be scared; relax, listen, watch the
highlighted sliders and frequency values on the screen, and let your brains do the job ;-)!*
- Second, you take a **test** which is nothing but a sequence of ten similar examples with randomly chosen frequency values 
and boost/cut options (where available), which you guess, and get a score to track your progress.

<br />

### Short Start Guide

<a id="short-start-guide">Let's get started!</a>
1. With pink noise, selected as an audio source, [switch the application to the Learn mode](#learn-mode), using the corresponding
button on the main window, the main menu item or the keyboard shortcut, or just by changing an [EQ slider](#equalization-sliders) handle position.
2. With pink noise examples, played in [the Learn mode](#learn-mode):
     * [Check/set up your audio playback system](#checking-audio-playback). 
     * [Adjust the volume level](#setting-volume-level).
3. [Make sure the frequency range/response of your playback audio system is decent enough](#checking-frequency-range).
4. In [the Learn mode](#learn-mode), with pink noise as an audio source and the first [equalization pattern](#eq-patterns),
go through all the possible examples.
5. Activate [the Test mode](#test-mode), and try to pass a test.
6. Repeat the learn-test cycle with the second and the third EQ patterns, using pink noise.
7. Save the volume level with the feature, available from the **Volume Slider** 
right-click context menu or from the **Audio** menu of the main menu. Then reduce the volume level by 10-15 dB.
8. [Load, preview and trim](#working-with-external-audio-files) some of your favorite commercially mastered music tracks of different
styles/genres.
9. Uncheck the **Controls | Start Playing After Loading Track in Preview Mode** option in the main menu if checked.
10. Restore the volume level with the feature, available from the **Volume Slider** 
right-click context menu or from the **Audio** menu of the main menu.
11. Do the learn-test exercises with the first three EQ patterns, using prepared music tracks.
12. Go through the other EQ patterns with both pink noise and music audio sources, thus increasing the difficulty step by step.
Adjust the volume level where needed.
13. After becoming familiar with the built-in EQ patterns, try practicing with custom [EQ Settings](#equalization-settings).
14. Explore more features, read more documentation (if needed).
<br />

### Choosing Acoustic Device
<a id="choosing-acoustic-device">If you can do</a> these exercises in a well treated room with studio quality monitors, it is great, 
but not obligatory. Decent consumer systems that do not add obvious distortion, crackling noises, etc. to sound 
at tolerably loud levels, and reproduce a wide frequency range 
([see further](#checking-frequency-range) about checking this), can also meet our requirements. 

You can use quality headphones as well. It is much easier and cheaper to achieve the accurate sound with them, 
one of the main reasons being that it is not affected by the room acoustics. Be aware, though, that pitch and loudness 
perception in headphones may significantly differ from the experience with loudspeakers. And you cannot feel the sound 
with your whole body this way, which may be especially important for analysing the lower end of the spectrum.
<br />

### Checking Audio Playback

<a id="checking-audio-playback">Obvious</a>, but important: make sure your audio system is switched on, and the playback audio path is working properly.
By default, the program uses your system sound output device. But you can easily switch to any available 
audio playback device, selecting **Audio | Audio Device** menu item from the main menu.

Initially, the audio source is set to **Pink noise** so that the software would not require any external files to 
get up and running. And it is usually the best starting point for your practice session. So, make sure the corresponding
option is selected in the **Audio Source** window.

Are you ready to hear the sound :-)? Just click the 
**Learn** mode button **or** change the position of any EQ sliders' handle by dragging/clicking on it, which will switch the application
to the *Learn* mode automatically. After some processing ([peak normalization](#peak-normalization) and equalization) and loading, which usually takes fractions of second
on contemporary machines, the playback of an example should start.

*Here, you may want to proceed with the training process. But I suggest that we should **adjust your
audio system** first.* <br />

### Adjusting Audio System
<a id="adjusting-audio-system">The flatter, the better</a>. I mean frequency response of your whole playback system, of course.
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
I have decided to apply to every audio source of single-band exercise the preventive [peak normalization](#peak-normalization) with opposite number to current absolute value
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
see details about [working with external audio files](#working-with-external-audio-files)).

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
<a id="eq-patterns">**EQ Pattern**</a> is a core of each exercise, as it defines:
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
<br />

#### Equalization Sliders
<a id="equalization-sliders">**EQ Sliders**</a> are the main input controllers for the training (**Learn** and **Test**) modes. The numbers below each of them
represent the central frequencies of corresponding frequency bands. And the positions of sliders' handles determine the boost or cut
of particular bands, whether real (while learning) or guessed (while testing).

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
<br />

#### Equalization Settings
<a id="equalization-settings">You can open the **EQ Settings**</a> by clicking the button with gear icon in the top-right corner
of the EQ or by selecting **View | EQ Settings** from the main menu.
They consist of two parameters: 
1. *Frequency Gain*, that determines an amount by which the center frequency of filter is boosted or cut.
2. *Bandwidth*/*Q factor*, that are used to set the width of boosted or cut frequency band.

Here is a filter frequency response scheme:

<br />

<img align="center" src=":/Getting_Started/Data/Images/BellFilterScheme.png"/>

This type of filter is called *peaking* or *bell* band-pass filter.
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

For *Bandwidth* options, I have used the values which can easily be thought of as music (tempered-scale) intervals:
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
will re-normalize your audio according to current Frequency Gain and EQ pattern. Clicking the **Reset** button restores 
default EQ pattern settings.

If you want to use the same settings across various EQ patterns, you can **Lock** them with the corresponding button.
For example, you have become confident with all the patterns, and you want to boost your proficiency. In this case,
while going through the same patterns, 
you can try lowering the frequency gain value, and challenge your ears to hear the subtler and subtler equalization.

When locked, this state and values themselves are stored between sessions.
<br />

### Working with External Audio Files

<a id="working-with-external-audio-files">There are</a> different ways to load external audio into the software:
- Select **File | Open Files...** from the main menu, or press **Ctrl+O** (on Windows) or 
**⌘O** (on macOS), or click on <span style="color:green; font-weight:bold">+</span> in the **Audio Source** window.
- Select **File | Open Folder...** from the main menu.
- Drag & Drop files/folders to the **Playlist** from anywhere possible.

The methods above can be used both for locating audio files of [the supported formats](#supported-audio-formats) directly
or through playlists. Currently, parsing of M3U, M3U8, PLS and XSPF playlists is supported.

After adding audio files to the **Playlist**, you can load each of them in various ways.
If you haven't loaded any audio file before, in case you manually switch the **Audio Source** to the **Audio File (Playlist)** mode,
clicking the **Play** button or choosing **Controls | Play** from the main menu will load and start playing the first track.
However, with **Shuffle Playback** option checked, a random audio file will be chosen. 

You can also load any track you want just by double-clicking on it or by selecting it and pressing *Enter*. This will switch the **Audio Source** to the 
**Audio File (Playlist)** mode automatically.

For further playlist navigation, you can use the <img src=":/Help_Icons/Data/Images/media-skip-backward_16.png"/> 
**Previous Track** / <img src=":/Help_Icons/Data/Images/media-skip-forward_16.png"/> **Next Track** player controls or similar buttons <img src=":/Help_Icons/Data/Images/arrows-right-and-left-filled-triangles.png"/> 
above the **Playlist**. 
When you are not in the **Preview** mode, the player skip controls/buttons are not available, though. In this case, if you want to go forward/backward
in the playlist, you can still use the navigation buttons above the **Playlist**. This will switch the program to the **Preview**
mode, whatever the current mode is. Any training process will be cancelled. Moreover, every change of an audio source resets the application to the **Preview** mode.
You can also manually activate the **Preview** mode by clicking the corresponding button on the main window or
by selecting **Controls | Preview Mode** from the main menu. The keyboard shortcut for it is  **Ctrl+P** (on Windows) or **⌘P** (on macOS).<br /> 

<img align="center" src=":/Getting_Started/Data/Images/PreviewMode.png"/><br />

On the first switch to **Audio File (Playlist)**, 
the **Transport Panel** becomes visible automatically. Here we may take the most advantage of the latter.<br />

<img align="center" src=":/Getting_Started/Data/Images/TransportPanel.png"/><br />

One of the main purposes of the **Preview** mode is to let a user select and **trim** an audio track region for further training. The white vs
gray zone(s) of the audio timeline slider at the **Transport Panel** represent the trimmed region inside a whole audio track.
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

Clicking the <img src=":/Help_Icons/Data/Images/clear.png"/>**Clear** button at the right of the start/end spin boxes resets the region bounds to default for newly loaded files, and
restores the previously saved values for already known ones.

The current **Playlist** and the latest audio source used are stored between sessions. However, I highly recommend 
saving the collections you would like to use repeatedly with **File | Export Playlist...** options.

> <img src=":/Help_Icons/Data/Images/lightbulb.png"/>***Useful Tip***
> 
> *Before doing training exercises in the **Learn** and the **Test** modes, prepare your own collection of trimmed audio files, 
using the above-described application tools. Then uncheck the **Controls | Start Playing After Loading Track in Preview Mode** 
option in the main menu if checked. [Adjust the volume level](#setting-volume-level) for your EQ Pattern and EQ Settings.
Load external audio files as audio sources for your exercises without playing them in the **Preview** mode. This will help you to
leave the volume knobs untouched as long as possible, while navigating through different audio sources/tracks.*
<br />

### The Learn Mode

<a id="learn-mode">The basic way</a> to activate the **Learn** mode is clicking the corresponding button on the main window or
by selecting **Controls | Learn Mode** from the main menu. The keyboard shortcut for it is  **Ctrl+L** (on Windows) or **⌘L** (on macOS).<br />
<img align="center" src=":/Getting_Started/Data/Images/LearnMode.png" /><br />

The application will normalize the audio if needed. When you use an external audio file as a source, the program 
will read and crop it before that.
Then the playback of the first example will start automatically.

On each example playback, the corresponding EQ sliders' handles change their positions. And when the EQ is on, these sliders
are highlighted in green, and their labels show if the frequencies are boosted <span style="color:green; font-weight:bold">(+)</span>
or cut <span style="color:green; font-weight:bold">(-)</span>.

If you want to stop the playback of an example, use the **Stop** control/button or press the dot *(.)* key. To start playing the example once again, click 
the **Play** control/button or press the *Space* key. You can change the **EQ settings** between the playbacks. If you set another **Frequency Gain**,
the audio would be re-normalized.

By default, the EQ bands are played in the ascending order; if both boosting and cutting are available in the current
EQ pattern, each band is first boosted, then cut before proceeding to the next one. However, you can optionally change
this order to the descending or the shuffle one, selecting the appropriate option in **Controls | EQ Bands Order in Learn Mode** menu
of the main menu. In boost & cut exercises, you can set the order with the sequence of all the bands boosted, and then 
all bands cut (or vice-versa), by selecting the option **All Bands Boosted, then All Bands Cut** in the same menu.

To go to the next example, click the <img src=":/Getting_Started/Data/Images/next-example.png"/> **Next Example** control/button,
or press **Ctrl+Return** (on Windows) or **⌘+Return** (on macOS).

Alternatively, you can check the option <img src=":/Getting_Started/Data/Images/sequential-playback.png"/> **Sequential Playback (of Learning Examples)** 
in the **Controls** menu of the main menu or in the **Transport Panel**. In this case, you can start the playback once, and then
the application will make and play each next example automatically. With **Controls | Loop Sequence (of EQ Bands)** unchecked,
it will stop after all possible EQ sliders' positions within the current EQ pattern have been gone through. Checking
this option will result in infinite loop until the playback is stopped.

Moving a slider handle (or two slider handles for dual-band patterns) will force the boost/cut of certain frequency band(s), and
this will become the first element of a sequence regardless of the EQ bands order set.
<br />

### The Test Mode

<a id="test-mode">The **Test** mode</a> is activated by clicking the corresponding button on the main window or
by selecting **Controls | Test Mode** from the main menu. The keyboard shortcut for it is  **Ctrl+T** (on Windows) or 
**⌘T** (on macOS).<br />
<img align="center" src=":/Getting_Started/Data/Images/TestMode.png" /><br />

The application will normalize the audio if needed. When you use an external audio file as a source, the program will 
read and crop it before that. Then the playback of the first example will start automatically.

To complete a test, you should do ten examples in a row. [Use sliders' handles to input the guessed answers](#equalization-sliders).
This can be done during or after the playback of each example. Once your answer is accepted, the right answer 
will be labelled and highlighted in green immediately. The <img src=":/Getting_Started/Data/Images/next-example.png"/> **Next Example** control/button
will become enabled so that you could proceed.  Unlike in the **Learn** mode, the sliders with changed handles' positions (the user input)
may differ from the highlighted ones (the right answer).

You can play and stop a current example as many times as you want with the **Play** and the **Stop** buttons/controls correspondingly.
Any time you do not give the exact right answer, it is highly recommended to play the example once again for better training effectiveness.

When the mode is activated, the **Exercise / Score Information** window is shown. It contains useful information about a current test:
examples count, test status (in progress, finished with pass/fail or canceled), the user and the right answers, and scoring.

The score calculation is quite straightforward. The maximum score for an example is 10, and the maximum total score for a test is 100.
When a user's answer is equal to the right answer, he or she gets 10 out of 10. Each 1-octave error subtracts 1 score point. Each 1/3-octave
error subtracts 0.33 points. The boost/cut mistake takes off 2 points. In case of dual-band exercise, the scores for each frequency band
in an example are count separately, with 5 being the maximum and 0 being the minimum for a frequency band. And then a maximum possible sum is taken as the 
score for the example.

The following table shows the expected score range for different types of exercises (EQ patterns):

| Exercise / EQ Pattern Type | Expected Score |
|:---------------------------|:--------------:|
| 1-octave bands, single-band|  85&mdash;95   |
| 1/3-octave bands, single-band|  75&mdash;90   |
| 1-octave bands, dual-band|  70&mdash;85   |
| 1/3-octave bands, dual-band|  65&mdash;80   |

<br />

To pass the test, you must get a total score which is 5 points below the lower end of the expected score range or higher. If your score is higher than
the upper end of the range, you get the *passed+* mark.

Changing EQ settings is disabled in this mode. Loading another audio source or switching to another mode would cancel 
the current test. Selecting another EQ Pattern would reset it as well.

<br />

### How to Memorize Frequency Bands?

<a id="memorizing-frequencies">Here are some tips</a> that could help you to memorize and internalize the frequency bands. Think of them as of reference
points for your mind rather than direct guidance. They may be more or less helpful, depending on different factors:
personal skills, experience, peculiarities of perception, kind of audio material, equalization settings, listening conditions, etc.

<img src=":/Help_Icons/Data/Images/lightbulb.png"/>If you are a musician, and especially if you have a perfect pitch, trying to
mentally connect center frequencies of band-pass filters with musical notes, closest to them, may be a good place to start.
This works best with pink noise. [The higher the Q factor and the more the frequency gain](#equalization-settings), the stronger the impression of a certain pitch.

Here is a screenshot of the 30-band in-app EQ with labels of musical notes that *approximately* match the filters' center frequencies.<br />

<img align="center" src=":/Getting_Started/Data/Images/Frequency-Note.png"/><br />

Musical instruments manufacturers and software developers often use different octave numerations. We use the 
*Scientific pitch notation (SPN)*, also known as *American standard pitch notation (ASPN)* and *international pitch notation (IPN)* here.
So, we consider that C4 is the *middle C* (~260 Hz), and the exact audio frequency of A4 is 440 Hz.<br />

<img align="center" src=":/Getting_Started/Data/Images/C4_A4.png"/><br />

This method can be applied to some extent to music as well, especially in certain cases when frequency bands contain the fundamental frequencies of musical 
instruments. You might notice, how equalization changes loudness of different notes or relationship between fundamentals and harmonics/overtones.
But for music, the approach would generally work as a positive side effect of timbre/pitch associations.<br />

<img src=":/Help_Icons/Data/Images/lightbulb.png"/>For pink noise exercises, try to find connotations between different spectral
bands and certain "real" sounds, such as working engine, streamlet, waterfall, pouring sand, etc. For music exercises, think of resonating environments and objects
which may have an effect, similar to particular equalization: big and small boxes, bottles, jars, cans, pots, cars, rooms, bathrooms, caves, tunnels, anything you have had experience with.<br />

<img src=":/Help_Icons/Data/Images/lightbulb.png"/>When training with music, make (mental) notes of how altering different frequency bands
changes timbres of instruments/voices. There are some tables with attempts to verbally describe different spectral ranges. However, using 
them may not be very helpful because the effect of particular equalization on timbre may drastically depend on a sound source, how it has been recorded,
the playback conditions, the amount of frequency gain, and other settings. Moreover, the alteration of the same frequency band
may be described as something that brings a positive or a negative quality under different conditions. E.g., fat and groovy vs boomy (low range boost),
full and warm vs muddy (low-mid range boost), clear vs thin (low-mid range cut), round, full and rich vs boxy and honky (mid range boost), bright vs harsh (high-mid and high range boost), 
smooth vs dull (high-mid and high range cut) and so on. Cutting one frequency band may have an effect similar to boosting another frequency band. 
So, instead of relying on someone's interpretations, try to make
your own descriptions, related to certain sound sources, settings and conditions.

<img src=":/Help_Icons/Data/Images/lightbulb.png"/>Recognizing cut frequencies is a bit harder than boosted ones. When the EQ is on, listen to
the frequencies left trying to figure out what is missing. When the EQ returns to its off state, think of it as of frequencies' boost. 

<img src=":/Help_Icons/Data/Images/lightbulb.png"/>What about synesthesia? The most primitive and obvious case of it, which you deal with here by training:
you hear frequencies, and see different activated sliders, each having its position in space, plus highlighted numbers. But can you see/imagine frequency bands as different colors/textures/material types?
Can you feel them? Can you smell them? Can you taste them? Try to note the slightest and subtlest body and mind reactions when listening to equalization examples, and focus on them for a moment.

*Try different approaches. Find out, what works better for you in different situations. Stay as relaxed as possible while training.
Take pauses. Do not torture your ears and brains too much.
Train regularly, not long: 2*&mdash;*4 exercises per session may be enough. 
Try to build your personal timbre/frequency vocabulary through daily practice!*

***And, last but not least. Even the small recurring donation to the project not only helps to support and develop the software, but it is a great source of additional motivation for you to
keep practicing!***

--------
### Annotations

#### Pink Noise

<a id="pink-noise">Pink noise</a> is a kind of random noise which has equal energy in different octave ranges. It derives from white noise which
is a random signal with wide frequency range and equal power for each frequency. Since the number of frequencies in octave doubles
for each octave increase, the energy of white noise doubles in each higher octave as well, which is 3 dB/oct. boost. In other words, white noise
gives the *impression* of high-frequencies dominance.
In pink noise, the energy falls proportionally to frequency. I.e., it is similar to white noise, but with 3 dB/octave attenuation, starting from 1 Hz. 
This gives a much more even result from a human ear perspective, and the spectrum of pink noise is the closest one to an average music signal.

[< Back to "The Basic Training Method"](#the-basic-training-method)

#### Peak Normalization

<a id="peak-normalization">Peak normalization</a> of an audio file or its part is a linear change of its whole gain that makes the amplitude level of its (PCM) sample 
with the maximum amplitude equal to a certain value (in dB).

[< Back to "Checking Audio Playback"](#checking-audio-playback)<br />
[< Back to "Setting Volume Level"](#setting-volume-level)

#### Supported Audio Formats
<a id="supported-audio-formats">The fully supported audio formats</a> are: WAVE, AIFF, MP3 and FLAC. The OGG format is half-supported.
OGG audio files can be added to the **Playlist**, but they cannot be played with the current media
player backend neither on Windows nor on macOS. If you try to load an OGG file, you will get the error message
with option to proceed with conversion to WAVE or AIFF. There is also a known backend issue with incorrect FLAC files'
playback position on macOS, which may occur when starting playing from a non-zero position. To work around
these format problems, you can [convert audio files to WAVE or AIFF](https://earquiz.org/manuals/earquiz-frequencies-help/converting-audio/) beforehand by selecting them and choosing 
**File | Convert Selected Files...** from the main menu or the similar option from the right-click context menu of the **Playlist**.

[< Back to "The Basic Training Method"](#the-basic-training-method)<br />
[< Back to "Working with External Audio Files"](#working-with-external-audio-files)
