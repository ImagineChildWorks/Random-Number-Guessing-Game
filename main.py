# Random Number Guessing game using Python | => Imagine ChildWorks

from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Ui_NumberGuessingGame(object):
    def rand(self):
        self.rnd = random.randint(1, 101)
        self.r = self.rnd + 10
        self.l = self.rnd - 10
        # print(self.rnd)
    def again(self):
        ag = self.ip.text()
        if ag.isdigit():
            if int(ag) == 1:
                self.no = 5
                self.w = 0
                self.rand()
                self.qn.setText("Enter a number between 1 to 100")
                self.info.setText("")
                self.chance.setText("5/5")
                self.ip.setText("")
            else:
                exit()
        else:
            exit()
    def clicked(self, ipt, num):
        if len(ipt) > 0:
            if self.no == -1:
                self.again()
                self.ip.setText("")
            else:
                if ipt.isdigit():
                    i = int(ipt)
                    if num > 0:
                        if self.rnd == i:
                            self.info.setText("You win!!!.\nThe number is : " + str(self.rnd))
                            self.no = 0
                            self.w = 1
                        else:
                            if self.l < i < self.rnd:
                                self.info.setText("Your guess is nearby lesser than the number")
                            elif self.rnd < i < self.r:
                                self.info.setText("Your guess is nearby greater than the number")
                            elif i < self.l:
                                self.info.setText("Your guess is too lesser")
                            elif self.r < i:
                                self.info.setText("Your guess is too greater")
                            txt = str(num-1) + "/5"
                            self.chance.setText(txt)
                            self.no -= 1
                    if self.no == 0:
                        if self.w == 0:
                            self.info.setText("You lose!!!.\nThe number is : " + str(self.rnd))
                        self.qn.setText("Would you like to continue\n(Yes[1]/No[otherwise])?")
                        self.no = -1
                else:
                    self.info.setText("Enter only a number!!!")
        else:
            self.info.setText("Enter an input first")
        self.ip.setText("")
    def setupUi(self, NumberGuessingGame):
        NumberGuessingGame.setObjectName("NumberGuessingGame")
        NumberGuessingGame.resize(800, 469)
        NumberGuessingGame.setMinimumSize(QtCore.QSize(800, 470))
        NumberGuessingGame.setMaximumSize(QtCore.QSize(800, 470))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Untitled.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NumberGuessingGame.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(NumberGuessingGame)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color : skyblue;")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(168, 30, 501, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.qn = QtWidgets.QLabel(self.centralwidget)
        self.qn.setGeometry(QtCore.QRect(210, 139, 421, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.qn.setFont(font)
        self.qn.setAlignment(QtCore.Qt.AlignCenter)
        self.qn.setObjectName("qn")
        self.ip = QtWidgets.QLineEdit(self.centralwidget)
        self.ip.setGeometry(QtCore.QRect(210, 230, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ip.setFont(font)
        self.ip.setText("")
        self.ip.setCursorPosition(0)
        self.ip.setAlignment(QtCore.Qt.AlignCenter)
        self.ip.setObjectName("ip")
        self.ip.setStyleSheet("border : 1px solid black; border-bottom : 2px solid black; background-color : white;")
        self.info = QtWidgets.QLabel(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(210, 270, 421, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.info.setFont(font)
        self.info.setText("")
        self.info.setAlignment(QtCore.Qt.AlignCenter)
        self.info.setObjectName("info")
        self.info.setStyleSheet("color : blue;")
        self.no = 5
        self.rnd = 0
        self.r = 0
        self.l = 0
        self.w = 0
        self.rand()
        self.okb = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.clicked(self.ip.text(), self.no))
        self.okb.setGeometry(QtCore.QRect(570, 230, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.okb.setFont(font)
        self.okb.setObjectName("okb")
        self.okb.setStyleSheet("border : 1px solid black; background-color : white;")
        self.chance = QtWidgets.QLabel(self.centralwidget)
        self.chance.setGeometry(QtCore.QRect(715, 190, 41, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.temp = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.clicked(self.ip.text(), self.no))
        self.temp.setGeometry(QtCore.QRect(840, 388, 41, 20))
        self.temp.setObjectName("temp")
        self.chance.setFont(font)
        self.chance.setObjectName("chance")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(685, 160, 95, 70))
        self.label.setStyleSheet("border : 1px solid white; height : 530px; background : transparent;")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignTop)
        NumberGuessingGame.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NumberGuessingGame)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        NumberGuessingGame.setMenuBar(self.menubar)

        self.retranslateUi(NumberGuessingGame)
        QtCore.QMetaObject.connectSlotsByName(NumberGuessingGame)

    def retranslateUi(self, NumberGuessingGame):
        _translate = QtCore.QCoreApplication.translate
        NumberGuessingGame.setWindowTitle(_translate("NumberGuessingGame", "Number Guessing Game"))
        self.title.setText(_translate("NumberGuessingGame", "NUMBER GUESSING GAME"))
        self.qn.setText(_translate("NumberGuessingGame", "Enter a number between 1 to 100"))
        self.okb.setText(_translate("NumberGuessingGame", "OK"))
        self.okb.setShortcut(_translate("NumberGuessingGame", "Enter"))
        self.chance.setText(_translate("NumberGuessingGame", "5/5"))
        self.label.setText(_translate("NumberGuessingGame", "Chances left :"))
        self.temp.setText(_translate("NumberGuessingGame", "PushButton"))
        self.temp.setShortcut(_translate("NumberGuessingGame", "Return"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NumberGuessingGame = QtWidgets.QMainWindow()
    ui = Ui_NumberGuessingGame()
    ui.setupUi(NumberGuessingGame)
    NumberGuessingGame.show()
    sys.exit(app.exec_())
