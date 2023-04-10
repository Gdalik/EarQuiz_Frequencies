import contextlib

from GUI import globals as gb


class PinkNoiseMode:
    def __init__(self, parent):  # parent: MainWindowContr
        self.parent = parent
        self.name = 'Pinknoise'
        self.view = parent.mw_view
        self.parent.SRC.savePrevSourceAudioRange()
        with contextlib.suppress(AttributeError):
            self.parent.AL.setNoAudio()
        self.default_slice_length = gb.default_pn_slice_length
        self.parent.TransportContr.TransportView.SliceLenSpin.setValue(gb.default_pn_slice_length)
        self.parent.setMakeAudioActionsEnabled(True)
        self.parent.AL.load_pinknoise()


class AudioFileMode:
    def __init__(self, parent):  # parent: MainWindowContr
        self.parent = parent
        self.name = 'Audiofile'
        self.view = parent.mw_view
        with contextlib.suppress(AttributeError):
            self.parent.AL.setNoAudio()
        self.default_slice_length = gb.default_audio_slice_length
        self.parent.TransportContr.TransportView.SliceLenSpin.setValue(gb.default_audio_slice_length)
        self.view.TransportPanel.show()
