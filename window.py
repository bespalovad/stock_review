# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 499)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.All = QtWidgets.QVBoxLayout()
        self.All.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.All.setObjectName("All")
        self.HeaderBox = QtWidgets.QGroupBox(self.centralwidget)
        self.HeaderBox.setStyleSheet("background-color: rgb(255, 149, 78)")
        self.HeaderBox.setObjectName("HeaderBox")
        self.Header = QtWidgets.QHBoxLayout(self.HeaderBox)
        self.Header.setContentsMargins(1, -1, -1, -1)
        self.Header.setObjectName("Header")
        self.LeftHeader = QtWidgets.QGroupBox(self.HeaderBox)
        self.LeftHeader.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LeftHeader.setStyleSheet("background-color: rgb(108, 231, 255)")
        self.LeftHeader.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.LeftHeader.setObjectName("LeftHeader")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.LeftHeader)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Menu_Button = QtWidgets.QPushButton(self.LeftHeader)
        self.Menu_Button.setMinimumSize(QtCore.QSize(50, 50))
        self.Menu_Button.setMaximumSize(QtCore.QSize(50, 50))
        self.Menu_Button.setStyleSheet("background-color: rgb(190, 124, 255)")
        self.Menu_Button.setObjectName("Menu_Button")
        self.horizontalLayout_2.addWidget(self.Menu_Button)
        self.Header.addWidget(self.LeftHeader, 0, QtCore.Qt.AlignLeft)
        self.RightHeader = QtWidgets.QWidget(self.HeaderBox)
        self.RightHeader.setStyleSheet("background-color: rgb(141, 255, 139)")
        self.RightHeader.setObjectName("RightHeader")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.RightHeader)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.RightHeaderBox = QtWidgets.QHBoxLayout()
        self.RightHeaderBox.setContentsMargins(100, 0, -1, -1)
        self.RightHeaderBox.setSpacing(0)
        self.RightHeaderBox.setObjectName("RightHeaderBox")
        self.Hide = QtWidgets.QPushButton(self.RightHeader)
        self.Hide.setMinimumSize(QtCore.QSize(50, 50))
        self.Hide.setMaximumSize(QtCore.QSize(50, 50))
        self.Hide.setStyleSheet("background-color:rgb(0, 255, 255)")
        self.Hide.setObjectName("Hide")
        self.RightHeaderBox.addWidget(self.Hide)
        self.Fullscreen = QtWidgets.QPushButton(self.RightHeader)
        self.Fullscreen.setMinimumSize(QtCore.QSize(50, 50))
        self.Fullscreen.setMaximumSize(QtCore.QSize(50, 50))
        self.Fullscreen.setStyleSheet("background-color:rgb(255, 0, 127)")
        self.Fullscreen.setObjectName("Fullscreen")
        self.RightHeaderBox.addWidget(self.Fullscreen)
        self.Exit = QtWidgets.QPushButton(self.RightHeader)
        self.Exit.setMinimumSize(QtCore.QSize(50, 50))
        self.Exit.setMaximumSize(QtCore.QSize(50, 50))
        self.Exit.setStyleSheet("background-color: rgb(255, 0, 255)")
        self.Exit.setObjectName("Exit")
        self.RightHeaderBox.addWidget(self.Exit)
        self.horizontalLayout.addLayout(self.RightHeaderBox)
        self.Header.addWidget(self.RightHeader, 0, QtCore.Qt.AlignRight)
        self.All.addWidget(self.HeaderBox, 0, QtCore.Qt.AlignTop)
        self.MainBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainBox.sizePolicy().hasHeightForWidth())
        self.MainBox.setSizePolicy(sizePolicy)
        self.MainBox.setStyleSheet("background-color: rgb(255, 0, 4)")
        self.MainBox.setObjectName("MainBox")
        self.MainBody = QtWidgets.QHBoxLayout(self.MainBox)
        self.MainBody.setObjectName("MainBody")
        self.LeftMenu = QtWidgets.QGroupBox(self.MainBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LeftMenu.sizePolicy().hasHeightForWidth())
        self.LeftMenu.setSizePolicy(sizePolicy)
        self.LeftMenu.setSizeIncrement(QtCore.QSize(0, 0))
        self.LeftMenu.setBaseSize(QtCore.QSize(0, 0))
        self.LeftMenu.setStyleSheet("background-color: rgb(26, 255, 0)")
        self.LeftMenu.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.LeftMenu.setObjectName("LeftMenu")
        self.Left = QtWidgets.QVBoxLayout(self.LeftMenu)
        self.Left.setContentsMargins(1, -1, -1, -1)
        self.Left.setObjectName("Left")
        self.Home = QtWidgets.QPushButton(self.LeftMenu)
        self.Home.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Home.sizePolicy().hasHeightForWidth())
        self.Home.setSizePolicy(sizePolicy)
        self.Home.setMinimumSize(QtCore.QSize(50, 50))
        self.Home.setMaximumSize(QtCore.QSize(50, 50))
        self.Home.setStyleSheet("background-color:rgb(255, 255, 0)")
        self.Home.setObjectName("Home")
        self.Left.addWidget(self.Home, 0, QtCore.Qt.AlignHCenter)
        self.Notifications = QtWidgets.QPushButton(self.LeftMenu)
        self.Notifications.setMinimumSize(QtCore.QSize(50, 50))
        self.Notifications.setMaximumSize(QtCore.QSize(50, 50))
        self.Notifications.setStyleSheet("background-color: rgb(255, 247, 0)")
        self.Notifications.setObjectName("Notifications")
        self.Left.addWidget(self.Notifications, 0, QtCore.Qt.AlignHCenter)
        self.Search = QtWidgets.QPushButton(self.LeftMenu)
        self.Search.setMinimumSize(QtCore.QSize(50, 50))
        self.Search.setMaximumSize(QtCore.QSize(50, 50))
        self.Search.setStyleSheet("background-color: rgb(255, 247, 0)")
        self.Search.setObjectName("Search")
        self.Left.addWidget(self.Search, 0, QtCore.Qt.AlignHCenter)
        self.Settings = QtWidgets.QPushButton(self.LeftMenu)
        self.Settings.setMinimumSize(QtCore.QSize(50, 50))
        self.Settings.setMaximumSize(QtCore.QSize(50, 50))
        self.Settings.setStyleSheet("background-color: rgb(255, 247, 0)")
        self.Settings.setObjectName("Settings")
        self.Left.addWidget(self.Settings, 0, QtCore.Qt.AlignHCenter)
        self.MainBody.addWidget(self.LeftMenu, 0, QtCore.Qt.AlignTop)
        self.MainMenu = QtWidgets.QWidget(self.MainBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainMenu.sizePolicy().hasHeightForWidth())
        self.MainMenu.setSizePolicy(sizePolicy)
        self.MainMenu.setStyleSheet("background-color:rgb(255, 152, 255)")
        self.MainMenu.setObjectName("MainMenu")
        self.Central = QtWidgets.QVBoxLayout(self.MainMenu)
        self.Central.setObjectName("Central")
        self.MainBody.addWidget(self.MainMenu)
        self.RightMenu = QtWidgets.QGroupBox(self.MainBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RightMenu.sizePolicy().hasHeightForWidth())
        self.RightMenu.setSizePolicy(sizePolicy)
        self.RightMenu.setMinimumSize(QtCore.QSize(100, 0))
        self.RightMenu.setStyleSheet("background-color:rgb(21, 0, 255)")
        self.RightMenu.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.RightMenu.setObjectName("RightMenu")
        self.Right = QtWidgets.QVBoxLayout(self.RightMenu)
        self.Right.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.Right.setContentsMargins(0, 0, 0, 0)
        self.Right.setSpacing(0)
        self.Right.setObjectName("Right")
        self.pushButton = QtWidgets.QPushButton(self.RightMenu)
        self.pushButton.setObjectName("pushButton")
        self.Right.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.RightMenu)
        self.pushButton_2.setObjectName("pushButton_2")
        self.Right.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.RightMenu)
        self.pushButton_3.setObjectName("pushButton_3")
        self.Right.addWidget(self.pushButton_3)
        self.MainBody.addWidget(self.RightMenu, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.All.addWidget(self.MainBox)
        self.Footer = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Footer.sizePolicy().hasHeightForWidth())
        self.Footer.setSizePolicy(sizePolicy)
        self.Footer.setMinimumSize(QtCore.QSize(0, 50))
        self.Footer.setStyleSheet("background-color: rgb(9, 0, 63)")
        self.Footer.setObjectName("Footer")
        self.label_12 = QtWidgets.QLabel(self.Footer)
        self.label_12.setGeometry(QtCore.QRect(110, 20, 47, 13))
        self.label_12.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_12.setObjectName("label_12")
        self.All.addWidget(self.Footer)
        self.gridLayout.addLayout(self.All, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Menu_Button.setText(_translate("MainWindow", "Menu Button"))
        self.Hide.setText(_translate("MainWindow", "Hide"))
        self.Fullscreen.setText(_translate("MainWindow", "Fullscreen"))
        self.Exit.setText(_translate("MainWindow", "Exit"))
        self.Home.setText(_translate("MainWindow", "Home"))
        self.Notifications.setText(_translate("MainWindow", "Notifications"))
        self.Search.setText(_translate("MainWindow", "Search"))
        self.Settings.setText(_translate("MainWindow", "Settings"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.label_12.setText(_translate("MainWindow", "Footer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
