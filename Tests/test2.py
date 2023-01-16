import time

from pedalboard.io import AudioFile
from Model.AudioEngine.load_audio import AudioChunk
from Model.AudioEngine.process import eq_proc

fn = 'Agutin_mono'
a = time.time()
with AudioFile(f'Audio/{fn}.wav') as f:
    chunk = AudioChunk(f, 0, 15)

    with AudioFile(f'Audio/{fn}_chunk1.wav', 'w', f.samplerate, f.num_channels) as o:
        o.write(chunk.croped)
    with AudioFile(f'Audio/{fn}_chunk1_norm.wav', 'w', f.samplerate, f.num_channels) as o:
        o.write(chunk.normalize(-16))
    eqed = eq_proc(chunk.croped, chunk.samplerate, freq1=1000, boost_cut1='+', freq2=16000, boost_cut2='-', gain_depth=15)
    # eqed = eq_proc(chunk.croped, chunk.samplerate, freq1=16000, gain_depth=15)
    with AudioFile(f'Audio/{fn}_chunk1_norm_eq.wav', 'w', f.samplerate, f.num_channels) as o:
        o.write(eqed)
print(time.time()-a)
