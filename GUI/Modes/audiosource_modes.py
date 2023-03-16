default_pn_slice_length = 10
default_audio_slice_length = 12


class PinkNoiseMode:
    def __init__(self, parent):     # parent: MainWindowContr
        self.parent = parent
        self.name = 'Pinknoise'
        self.view = parent.mw_view
        self.parent.setNoAudio()
        self.parent.TransportContr.TransportView.SliceLenSpin.setValue(default_pn_slice_length)
        self.parent.load_pinknoise()


class AudioFileMode:
    def __init__(self, parent):     # parent: MainWindowContr
        self.parent = parent
        self.name = 'Audiofile'
        self.view = parent.mw_view
        self.parent.setNoAudio()
        self.parent.TransportContr.TransportView.SliceLenSpin.setValue(default_audio_slice_length)
        self.view.TransportPanel.show()
