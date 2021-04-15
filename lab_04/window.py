# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1225, 900)
        MainWindow.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(889, 820, 311, 41))
        self.exit_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.exit_btn.setObjectName("exit_btn")
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(890, 770, 311, 41))
        self.clear_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.clear_btn.setObjectName("clear_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(890, 390, 311, 41))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.xc_lbl = QtWidgets.QLineEdit(self.centralwidget)
        self.xc_lbl.setGeometry(QtCore.QRect(920, 450, 121, 31))
        self.xc_lbl.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.xc_lbl.setObjectName("xc_lbl")
        self.yc_lbl = QtWidgets.QLineEdit(self.centralwidget)
        self.yc_lbl.setGeometry(QtCore.QRect(1080, 450, 121, 31))
        self.yc_lbl.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.yc_lbl.setObjectName("yc_lbl")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1050, 440, 21, 41))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(890, 440, 21, 41))
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1020, 20, 85, 22))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1010, 100, 121, 22))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1030, 180, 51, 22))
        self.label_9.setObjectName("label_9")
        self.analysis = QtWidgets.QPushButton(self.centralwidget)
        self.analysis.setGeometry(QtCore.QRect(890, 720, 311, 41))
        self.analysis.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.analysis.setObjectName("analysis")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1010, 540, 71, 22))
        self.label_10.setObjectName("label_10")
        self.spectrum_btn = QtWidgets.QPushButton(self.centralwidget)
        self.spectrum_btn.setGeometry(QtCore.QRect(890, 670, 311, 41))
        self.spectrum_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spectrum_btn.setObjectName("spectrum_btn")
        self.draw_btn = QtWidgets.QPushButton(self.centralwidget)
        self.draw_btn.setGeometry(QtCore.QRect(890, 490, 311, 41))
        self.draw_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.draw_btn.setObjectName("draw_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1225, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.exit_btn.setText(_translate("MainWindow", "Выход"))
        self.clear_btn.setText(_translate("MainWindow", "Очистить поле"))
        self.label.setText(_translate("MainWindow", "              Координаты центра:"))
        self.label_3.setText(_translate("MainWindow", "У:"))
        self.label_2.setText(_translate("MainWindow", "Х:"))
        self.label_7.setText(_translate("MainWindow", "Режим"))
        self.label_8.setText(_translate("MainWindow", "Алгоритм"))
        self.label_9.setText(_translate("MainWindow", "Цвет"))
        self.analysis.setText(_translate("MainWindow", "Сравнение алгоритмов"))
        self.label_10.setText(_translate("MainWindow", "Спектр"))
        self.spectrum_btn.setText(_translate("MainWindow", "Построить спектр"))
        self.draw_btn.setText(_translate("MainWindow", "Построить окружность"))