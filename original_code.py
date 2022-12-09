class Television:

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self):
        if not self.__muted:
            self.__muted = True
        else:
            self.__status = False

    def channel_up(self):
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        if self.__status and self.__volume < Television.MAX_VOLUME:
            self.__volume += 1

    def volume_down(self):
        if self.__status and self.__volume > Television.MIN_VOLUME:
            self.__volume -= 1

    def __str__(self):
        if self.mute:
            return f'TV status: Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}.'
        else:
            return f'TV status: Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}.'
