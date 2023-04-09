from definitions import Settings

default_pn_slice_length = None
default_audio_slice_length = None


def defaultSliceLenUpd():
    global default_pn_slice_length
    global default_audio_slice_length
    Settings.beginGroup('GlobalVars')
    default_pn_slice_length = int(Settings.value('PinknoiseSliceLength', 10))
    default_audio_slice_length = int(Settings.value('ExtAudioSliceLength', 12))
    Settings.endGroup()


defaultSliceLenUpd()
