from Model.AudioEngine.load_audio import AudioChunk
from pedalboard.io import AudioFile
from definitions import ROOT_DIR

fn = 'Aqualung'

with AudioFile(f'{ROOT_DIR}/Audio/{fn}.wav') as f:
    chunk = AudioChunk(f, 0, 0, slice_length=0)
    print(f'{chunk.starttime} - {chunk.endtime}')
    #chunk.endtime = 15
    '''chunk.normalize(-12)
    for i in range(1):
        with AudioFile(f'{ROOT_DIR}/Audio/{fn}_chunk{i+1}.wav', 'w', f.samplerate, f.num_channels) as o:
            o.write(chunk.slice_iter())
    chunk.endtime = 30
    chunk.starttime = 10
    print(f'{chunk.starttime} - {chunk.endtime}')
    with AudioFile(f'{ROOT_DIR}/Audio/{fn}_chunk_new.wav', 'w', f.samplerate, f.num_channels) as o:
            o.write(chunk.slice_iter())'''
