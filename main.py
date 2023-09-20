import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.buttons=[[self.ui.btn_1,self.ui.btn_2,self.ui.btn_3,self.ui.btn_4],
                        [self.ui.btn_5,self.ui.btn_6,self.ui.btn_7,self.ui.btn_8],
                        [self.ui.btn_9,self.ui.btn_10,self.ui.btn_11,self.ui.btn_12],
                        [self.ui.btn_13,self.ui.btn_14,self.ui.btn_15,self.ui.btn_16]]
        
        random_list=[]
        n=0
        for i in range(4):
            for j in range(4):
                n += 1 #شمارنده برای تعداد عددهایی که جدول را پر کرده
                while True:
                    r=random.randint(1,16)
                    random_list.append(r)
                    if len(set(random_list))==n:
                        self.buttons[i][j].setText(str(r))
                        self.buttons[i][j].clicked.connect(partial(self.play,i,j))
                        if r==16:
                            self.buttons[i][j].setVisible(False)
                            self.empty_i = i
                            self.empty_j = j
                        break

    def play(self,i,j):
        if (i==self.empty_i and abs(j-self.empty_j)==1) or \
            (j==self.empty_j and abs(i-self.empty_i)==1):
            
            self.buttons[self.empty_i][self.empty_j].setText(self.buttons[i][j].text())
            self.buttons[i][j].setText("16")

            self.buttons[self.empty_i][self.empty_j].setVisible(True)
            self.buttons[i][j].setVisible(False)

            self.empty_i=i
            self.empty_j=j

        if self.check_win()==True:
            msg_box=QMessageBox()
            msg_box.setText("You Win👏👏")
            msg_box.exec()

    def check_win(self):
        index=1
        for i in range(4):
            for j in range(4):
                if int(self.buttons[i][j].text()) != index:
                    return False
                index += 1

        return True

app=QApplication(sys.argv)

main_window=MainWindow()
main_window.show()

app.exec()
