from controller import *


def main():

    app = QApplication([])
    window = Controller()
    window.show()
    app.excec_()


if __name__ == '__main__':
    main()