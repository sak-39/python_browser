import sys

from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication, QPushButton, QDesktopWidget, QDialog, QHBoxLayout)
from PyQt5.QtCore import QUrl
from PyQt5 import QtNetwork
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings

__program__ = 'Coldwolf'

def program_name():
    return __program__


class ColdwolfWindow(QWidget):

    def __init__(self, parent=None):
        super(ColdwolfWindow, self).__init__()

        self.initUI(parent=parent)

    def initUI(self, parent=None):

        initurl = 'https://www.google.com'

        self.browser = QWebEngineView()
        self.browser.load(QUrl(initurl))
        self.browser.resize(1000,600)
        self.browser.move(100,100)
        self.browser.setWindowTitle(program_name())

        self.browser.settings().setAttribute(QWebEngineSettings.WebRTCPublicInterfacesOnly, True)

        # button
        self.back_button = QPushButton('<<')
        self.back_button.clicked.connect(self.browser.back)

        self.forward_button = QPushButton('>>')
        self.forward_button.clicked.connect(self.browser.forward)

        self.reload_button = QPushButton('Reload')
        self.reload_button.clicked.connect(self.browser.reload)

        self.url_edit = QLineEdit()
        self.url_edit.returnPressed.connect(self.loadPage)

        self.browser.urlChanged.connect(self.updateUrl)

        self.home_button = QPushButton('Home')
        self.home_button.clicked.connect(self.homePage)

        # layout
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.back_button, 1, 0)
        grid.addWidget(self.forward_button, 1, 1)
        grid.addWidget(self.reload_button, 1, 2)
        grid.addWidget(self.url_edit, 1, 3, 1, 10)
        grid.addWidget(self.home_button, 1, 14)
        grid.addWidget(self.browser, 2, 0, 5, 15)

        self.setLayout(grid)
        if parent is None:
            self.resize(1200,700)
            self.center()
            self.setWindowTitle(program_name())
            self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def loadPage(self):
        move_url = QUrl(self.url_edit.text())
        self.browser.load(move_url)
        self.updateUrl

    def updateUrl(self):
        self.url_edit.clear()
        self.url_edit.insert(self.browser.url().toString())

    def homePage(self):
        move_url = QUrl('https://twitter.com/home')
        self.browser.load(move_url)
        self.updateUrl


if __name__ == '__main__':

    app = QApplication(sys.argv)

    use_tor = 0
    if use_tor == 1:
        proxy = QtNetwork.QNetworkProxy()
        proxy.setType(QtNetwork.QNetworkProxy.Socks5Proxy)
        proxy.setHostName("127.0.0.1")
        proxy.setPort(9050)
        QtNetwork.QNetworkProxy.setApplicationProxy(proxy)

    ex = ColdwolfWindow()
    sys.exit(app.exec_())
