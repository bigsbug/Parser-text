# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(731, 460)
        Dialog.setMinimumSize(QtCore.QSize(731, 460))
        Dialog.setMaximumSize(QtCore.QSize(731, 460))
        Dialog.setSizeIncrement(QtCore.QSize(700, 410))
        self.Button_clear_Symbols = QtWidgets.QPushButton(Dialog)
        self.Button_clear_Symbols.setGeometry(QtCore.QRect(410, 400, 101, 25))
        self.Button_clear_Symbols.setObjectName("Button_clear_Symbols")
        self.Button_clear_english = QtWidgets.QPushButton(Dialog)
        self.Button_clear_english.setGeometry(QtCore.QRect(300, 400, 111, 25))
        self.Button_clear_english.setObjectName("Button_clear_english")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 51, 711, 311))
        self.plainTextEdit.setMaximumSize(QtCore.QSize(759, 484))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.Button_Erase = QtWidgets.QPushButton(Dialog)
        self.Button_Erase.setGeometry(QtCore.QRect(440, 370, 81, 25))
        self.Button_Erase.setObjectName("Button_Erase")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(520, 370, 81, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(600, 370, 81, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 370, 111, 25))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_swap_words = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_swap_words.setGeometry(QtCore.QRect(120, 370, 171, 25))
        self.lineEdit_swap_words.setInputMask("")
        self.lineEdit_swap_words.setText("")
        self.lineEdit_swap_words.setPlaceholderText("")
        self.lineEdit_swap_words.setObjectName("lineEdit_swap_words")
        self.Button_Limit_words = QtWidgets.QPushButton(Dialog)
        self.Button_Limit_words.setGeometry(QtCore.QRect(10, 400, 111, 25))
        self.Button_Limit_words.setObjectName("Button_Limit_words")
        self.spinBox_limit_wrods = QtWidgets.QSpinBox(Dialog)
        self.spinBox_limit_wrods.setGeometry(QtCore.QRect(120, 399, 171, 27))
        self.spinBox_limit_wrods.setObjectName("spinBox_limit_wrods")
        self.Button_Resize_spaces = QtWidgets.QPushButton(Dialog)
        self.Button_Resize_spaces.setEnabled(True)
        self.Button_Resize_spaces.setGeometry(QtCore.QRect(510, 400, 101, 25))
        self.Button_Resize_spaces.setObjectName("Button_Resize_spaces")
        self.Button_clear_Numbers = QtWidgets.QPushButton(Dialog)
        self.Button_clear_Numbers.setEnabled(True)
        self.Button_clear_Numbers.setGeometry(QtCore.QRect(610, 400, 111, 25))
        self.Button_clear_Numbers.setObjectName("Button_clear_Numbers")
        self.Button_Add_Dot = QtWidgets.QPushButton(Dialog)
        self.Button_Add_Dot.setGeometry(QtCore.QRect(360, 370, 81, 25))
        self.Button_Add_Dot.setObjectName("Button_Add_Dot")
        self.Button_Fetch = QtWidgets.QPushButton(Dialog)
        self.Button_Fetch.setGeometry(QtCore.QRect(90, 10, 91, 25))
        self.Button_Fetch.setObjectName("Button_Fetch")
        self.lineEdit_Key_Word = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Key_Word.setGeometry(QtCore.QRect(180, 10, 481, 25))
        self.lineEdit_Key_Word.setInputMask("")
        self.lineEdit_Key_Word.setText("")
        self.lineEdit_Key_Word.setObjectName("lineEdit_Key_Word")
        self.spinBox_Number_Pages = QtWidgets.QSpinBox(Dialog)
        self.spinBox_Number_Pages.setGeometry(QtCore.QRect(660, 9, 53, 27))
        self.spinBox_Number_Pages.setWrapping(False)
        self.spinBox_Number_Pages.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox_Number_Pages.setMinimum(1)
        self.spinBox_Number_Pages.setMaximum(10)
        self.spinBox_Number_Pages.setObjectName("spinBox_Number_Pages")
        self.radioButton_Google = QtWidgets.QRadioButton(Dialog)
        self.radioButton_Google.setGeometry(QtCore.QRect(10, 23, 81, 23))
        self.radioButton_Google.setChecked(True)
        self.radioButton_Google.setObjectName("radioButton_Google")
        self.radioButton_Bing = QtWidgets.QRadioButton(Dialog)
        self.radioButton_Bing.setGeometry(QtCore.QRect(10, 4, 81, 23))
        self.radioButton_Bing.setObjectName("radioButton_Bing")
        self.lineEdit_Titiles = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Titiles.setGeometry(QtCore.QRect(120, 430, 601, 25))
        self.lineEdit_Titiles.setInputMask("")
        self.lineEdit_Titiles.setText("")
        self.lineEdit_Titiles.setObjectName("lineEdit_Titiles")
        self.Button_Title = QtWidgets.QPushButton(Dialog)
        self.Button_Title.setGeometry(QtCore.QRect(10, 430, 111, 25))
        self.Button_Title.setObjectName("Button_Title")

        self.retranslateUi(Dialog)
        self.Button_Erase.clicked.connect(self.plainTextEdit.clear)
        self.pushButton_5.clicked.connect(self.plainTextEdit.paste)
        self.pushButton_4.clicked.connect(self.plainTextEdit.selectAll)
        self.pushButton_4.clicked.connect(self.plainTextEdit.copy)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Praser Text"))
        self.Button_clear_Symbols.setText(_translate("Dialog", "Clear symbols"))
        self.Button_clear_english.setText(_translate("Dialog", "Clear English"))
        self.Button_Erase.setText(_translate("Dialog", "Earse"))
        self.pushButton_4.setText(_translate("Dialog", "Copy"))
        self.pushButton_5.setText(_translate("Dialog", "Paste"))
        self.pushButton.setText(_translate("Dialog", "Swap words"))
        self.lineEdit_swap_words.setToolTip(_translate("Dialog", "Enter number swap word with spase like 1 8 9"))
        self.Button_Limit_words.setText(_translate("Dialog", "Limit word"))
        self.Button_Resize_spaces.setText(_translate("Dialog", "Resize spaces"))
        self.Button_clear_Numbers.setText(_translate("Dialog", "Clear Numbers"))
        self.Button_Add_Dot.setText(_translate("Dialog", "Dot"))
        self.Button_Fetch.setText(_translate("Dialog", "Fetch"))
        self.lineEdit_Key_Word.setToolTip(_translate("Dialog", "Enter number swap word with spase like 1 8 9"))
        self.lineEdit_Key_Word.setPlaceholderText(_translate("Dialog", "                                                                    keyword "))
        self.radioButton_Google.setText(_translate("Dialog", "Google"))
        self.radioButton_Bing.setText(_translate("Dialog", "Bing"))
        self.lineEdit_Titiles.setToolTip(_translate("Dialog", "Enter number swap word with spase like 1 8 9"))
        self.lineEdit_Titiles.setPlaceholderText(_translate("Dialog", "                                                                             Title"))
        self.Button_Title.setText(_translate("Dialog", "Title "))
