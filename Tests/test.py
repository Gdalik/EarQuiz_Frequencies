import numpy as np
from pedalboard import Pedalboard, Chorus, Reverb, PeakFilter, Compressor
from pedalboard.io import AudioFile

# Make a Pedalboard object, containing multiple audio plugins:
#board = Pedalboard([Chorus(), Reverb(room_size=0.25)])
eq = PeakFilter(cutoff_frequency_hz=1000, gain_db=12.0, q=3)
eq.gain_db = 6
# Open an audio file for reading, just like a regular file:
with AudioFile('Audio/pink_noise.wav') as f:
    print(f.frames / f.samplerate)
    file = f.read(f.frames)
    file_abs = np.absolute(file)
    db = 20*np.emath.log10(file_abs)
    print(file_abs)
    print(db)

    # Open an audio file to write to:
    with AudioFile('Audio/Aqualung_eq3.wav', 'w', f.samplerate, f.num_channels) as o:
        # Read one second of audio at a time, until the file is empty:
        while f.tell() < f.samplerate * 10:
            chunk = f.read(int(f.samplerate))
            print(chunk)

            # Run the audio through our pedalboard:
            #effected = eq.process(chunk, f.samplerate, reset=False)

            # Write the output to our output file:
            #o.write(effected)