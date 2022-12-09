from PyQt5.QtWidgets import *
from view_tv import *


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.power_button.clicked.connect(lambda: self.power())
        self.volume_up_button.clicked.connect(lambda: self.volume_up())
        self.volume_down_button.clicked.connect(lambda: self.volume_down())
        self.mute_button.clicked.connect(lambda: self.mute())
        self.channel_up_button.clicked.connect(lambda: self.channel_up())
        self.channel_down_button.clicked.connect(lambda: self.channel_down())
        self.netflix_button.clicked.connect(lambda: self.netflix())
        self.__status = False
        self.__muted = False
        self.__volume = Controller.MIN_VOLUME
        self.__channel = Controller.MIN_CHANNEL
        self.volume_slider.setValue(self.__volume)

    def tv_screen(self):
        if not self.__status:
            self.tv_output.clear()
        else:
            if self.__channel == 0:
                self.tv_output.setPixmap(QtGui.QPixmap('CNN.png'))
            elif self.__channel == 1:
                self.tv_output.setPixmap(QtGui.QPixmap('HBO.png'))
            elif self.__channel == 2:
                self.tv_output.setPixmap(QtGui.QPixmap('ESPN.png'))
            elif self.__channel == 3:
                self.tv_output.setPixmap(QtGui.QPixmap('NETFLIX.png'))



    def power(self):
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

        Controller.tv_screen(self)

    def volume_up(self):
        if self.__status and not self.__muted and self.__volume < Controller.MAX_VOLUME:
            self.__volume += 1
            self.volume_slider.setValue(self.__volume)

    def volume_down(self):
        if self.__status and not self.__muted and self.__volume > Controller.MIN_VOLUME:
            self.__volume -= 1
            self.volume_slider.setValue(self.__volume)

    def mute(self):
        if self.__status:
            if not self.__muted:
                self.__muted = True
                self.volume_down_button.setStyleSheet('color:gray;')
                self.volume_up_button.setStyleSheet('color:gray;')
                self.label.setStyleSheet('color:gray;')
            else:
                self.__muted = False
                self.volume_down_button.setStyleSheet("color: rgb(255, 255, 255);")
                self.volume_up_button.setStyleSheet("color: rgb(255, 255, 255);")
                self.label.setStyleSheet("color: rgb(255, 255, 255);")

    def channel_up(self):
        if self.__status:
            if self.__channel == Controller.MAX_CHANNEL:
                self.__channel = Controller.MIN_CHANNEL
            else:
                self.__channel += 1
        Controller.tv_screen(self)
    def channel_down(self):
        if self.__status:
            if self.__channel == Controller.MIN_CHANNEL:
                self.__channel = Controller.MAX_CHANNEL
            else:
                self.__channel -= 1
        Controller.tv_screen(self)

    def netflix(self):
        if self.__status:
            self.__channel = Controller.MAX_CHANNEL
        Controller.tv_screen(self)









