from urllib import parse
import webbrowser


class SupportAppContr:
    def __init__(self, mw_contr):
        self.sharedURL = parse.quote('https://earquiz.org/frequencies', encoding='utf-8')
        self.mw_contr = mw_contr
        self.mw_view = mw_contr.mw_view
        self.mw_view.Facebook.clicked.connect(self.onFacebook_clicked)
        self.mw_view.BMC.clicked.connect(self.onBMC_clicked)
        self.mw_view.Patreon.clicked.connect(self.onPatreon_clicked)
        self.mw_view.Boosty.clicked.connect(self.onBoosty_clicked)

    def onFacebook_clicked(self):
        print('Facebook')

    def onBMC_clicked(self):
        webbrowser.open('https://www.buymeacoffee.com/gdalik')

    def onPatreon_clicked(self):
        webbrowser.open('https://www.patreon.com/EarQuiz')

    def onBoosty_clicked(self):
        webbrowser.open('https://boosty.to/earquiz')
