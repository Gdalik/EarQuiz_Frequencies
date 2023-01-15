from PySide6.QtWidgets import QWidget


class TransportPanelView:
    """@DynamicAttrs"""
    def __init__(self, mw_view):
        for W in mw_view.dockWidgetContents.findChildren(QWidget):
            self.__setattr__(W.objectName(), W)
        self.upd_VolumeLab()
        self.VolumeSlider.valueChanged.connect(self.upd_VolumeLab)
        self.AudioSlider.setBackground('w')

    def upd_VolumeLab(self):
        self.VolumePerc.setText(f'{self.VolumeSlider.value()}%')
