from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.QtCore import Qt

import random
import ui
import praser
from searcher import search_google , search_bing

import sys
class main(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = ui.Ui_Dialog()
        self.setWindowFlags(Qt.WindowMinimizeButtonHint|Qt.WindowCloseButtonHint)
        self.setFixedSize(self.width(), self.height())

        self.ui.setupUi(self)
        self.ui.Button_clear_english.clicked.connect(self.Clear_English)
        self.ui.Button_clear_Symbols.clicked.connect(self.Clear_Symbols)
        self.ui.Button_clear_Numbers.clicked.connect(self.Clear_Numbers)
        self.ui.Button_Resize_spaces.clicked.connect(self.Resize_Spaces)
        self.ui.Button_Add_Dot.clicked.connect(self.Add_Dot)
        
        self.ui.Button_Limit_words.clicked.connect(self.Limit_Words)
        self.ui.pushButton.clicked.connect(self.Swap_Words)
        
        self.ui.Button_Fetch.clicked.connect(self.Fetch)

        self.ui.Button_Title.clicked.connect(self.Add_Title)
    def RWC(self,data):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.setPlainText(data)

    def Fetch(self):
        keyword = self.ui.lineEdit_Key_Word.text()
        number_pages = self.ui.spinBox_Number_Pages.value()
        if self.ui.radioButton_Google.isChecked():
            self.RWC(search_google(keyword,number_pages))
        else:
            self.RWC(search_bing(keyword,number_pages))

    def Resize_Spaces(self):
        data = self.ui.plainTextEdit.toPlainText()
        data = praser.Re_Space(data)
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.setPlainText(data)

    def Clear_English(self):
        data = self.ui.plainTextEdit.toPlainText()
        new_data = praser.Clear_English(data)
        self.RWC(new_data)
    
    def Clear_Symbols(self):
        data = self.ui.plainTextEdit.toPlainText()
        new_data = praser.Clear_Symbols(data)
        self.RWC(new_data)

    def Limit_Words(self):
            data = self.ui.plainTextEdit.toPlainText()
            limit = self.ui.spinBox_limit_wrods.value()
            new_data = praser.Limit_Words(data,limit)
            self.RWC(new_data)
    
    def Swap_Words(self):
            str_data = self.ui.plainTextEdit.toPlainText()
            swap_list =str( self.ui.lineEdit_swap_words.text()).split(' ')
            swap_list = list(map(int,swap_list))
            new_data = praser.Swap_Word(str_data,swap_list)
            self.RWC(new_data)

    def Clear_Numbers(self):
        data = self.ui.plainTextEdit.toPlainText()
        new_data = praser.Clear_Numbers(data)
        self.RWC(new_data)
    
    def Add_Dot(self):
        data = self.ui.plainTextEdit.toPlainText()
        new_data = praser.Add_Dot(data)
        self.RWC(new_data)
    
    def Add_Title(self):
        Perfix_title = [
             'دانلود کامل','دانلود مستقیم'
             ,'نسخه جدید','ورژن جدید','بهترین و کاملترین'
            ,'به روز شد','کاملترین مجموعه در اینترنت'
            ,'جدیدترین مجموعه','بروزترین پکیج','فوق العاده و عالی'
            ,'آپدیت شد','دانلود با لینک مستقیم'
            ,'مهمترین نکات','بهترین بسته اینترنتی','ویرایش جدید'
            ,'با بهترین کیفیت','با کیفیت مناسب برای شما'
            ,'مجموعه جدید و بسیار عالی','بسته کامل از سایت','دانلود نسخه جدید و عالی'
              ]
        title = self.ui.lineEdit_Titiles.text()
        data = self.ui.plainTextEdit.toPlainText()
        self.RWC(praser.Random_Title(Perfix_title,title,data))

app = QApplication(sys.argv)
w = main()
w.show()
sys.exit(app.exec_())