#    EarQuiz Frequencies. Software for technical ear training on equalization.
#    Copyright (C) 2023, Gdaliy Garmiza.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from urllib import parse
from definitions import app
import webbrowser


class SupportAppContr:
    def __init__(self, mw_contr):
        self.sharedURL = 'https://earquiz.org/EQ_Frequencies/'
        self.sharedURL_q = parse.quote(self.sharedURL, encoding='utf-8')
        self.sharedText = parse.quote("Great free software for technical ear "
                                      "training on equalization under Windows and macOS: ")
        self.mw_contr = mw_contr
        self.mw_view = mw_contr.mw_view
        self.mw_view.Facebook.clicked.connect(self.onFacebook_clicked)
        self.mw_view.VK.clicked.connect(self.onVK_clicked)
        self.mw_view.Twitter.clicked.connect(self.onTwitter_clicked)
        self.mw_view.BMC.clicked.connect(self.onBMC_clicked)
        self.mw_view.Patreon.clicked.connect(self.onPatreon_clicked)
        self.mw_view.Boosty.clicked.connect(self.onBoosty_clicked)
        self.mw_view.CopyLink.clicked.connect(self.onCopyLink_clicked)
        self.mw_view.WhatsApp.clicked.connect(self.onWhatsApp_clicked)
        self.mw_view.Telegram.clicked.connect(self.onTelegram_clicked)
        self.mw_view.Reddit.clicked.connect(self.onReddit_clicked)

    def onFacebook_clicked(self):
        webbrowser.open(f'https://www.facebook.com/sharer/sharer.php?u={self.sharedURL_q}')

    def onTwitter_clicked(self):
        webbrowser.open(f'https://twitter.com/intent/tweet?text={self.sharedText}{self.sharedURL_q}')

    def onCopyLink_clicked(self):
        app.clipboard().setText(self.sharedURL)
        self.mw_view.status.TempLabel.update('Link to EarQuiz Frequencies copied to clipboard.')

    def onBMC_clicked(self):
        webbrowser.open('https://www.buymeacoffee.com/gdalik')

    def onPatreon_clicked(self):
        webbrowser.open('https://www.patreon.com/EarQuiz')

    def onBoosty_clicked(self):
        webbrowser.open('https://boosty.to/earquiz')

    def onWhatsApp_clicked(self):
        webbrowser.open(f'https://api.whatsapp.com/send/?text={self.sharedText}{self.sharedURL_q}')

    def onTelegram_clicked(self):
        webbrowser.open(f'https://t.me/share/url?url={self.sharedURL_q}&text={self.sharedText}')

    def onVK_clicked(self):
        webbrowser.open(f'https://vk.com/share.php?url={self.sharedURL}')

    def onReddit_clicked(self):
        webbrowser.open(f'https://reddit.com/submit?url={self.sharedURL_q}&title={self.sharedText}')
