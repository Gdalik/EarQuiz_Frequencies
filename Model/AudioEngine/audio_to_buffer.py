import io
import numpy as np
from pedalboard.io import AudioFile


def a2b(audio_data: np.array, samplerate: int) -> io.BytesIO:
    res = io.BytesIO()
    with AudioFile(res, "w", samplerate=samplerate, num_channels=audio_data.shape[0], format='wav') as file_obj:
        file_obj.write(audio_data)
    return res
