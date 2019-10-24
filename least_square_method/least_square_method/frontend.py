import sys
import functools
import itertools

import numpy as np
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QApplication, QMainWindow,  QPushButton,  QLabel, QErrorMessage, QMessageBox, QTableWidget, QTableWidgetItem, QLineEdit
from PyQt5.QtCore import  QSize, QRegExp
from PyQt5.QtGui import QRegExpValidator

import least_square_method


class MyWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)       
        self.setMinimumSize(QSize(600, 400))   

        self.create_table_coords()
        self.create_input_polynom_degree()
        self.create_button_calc()
        self.create_about()


    def create_table_coords(self):
        ROWS_COUNT = 10
        
        self.tbl_coords = QTableWidget(self)

        headers_horiz = ["x", "y", "ρ"]        
        self.tbl_coords.setColumnCount(len(headers_horiz))
        self.tbl_coords.setHorizontalHeaderLabels(headers_horiz)

        self.tbl_coords.setRowCount(ROWS_COUNT)

        self.tbl_coords.move(120, 0)
        self.tbl_coords.resize(330,340)
     
        for i in range(ROWS_COUNT):
            self.tbl_coords.setItem(i,0,QTableWidgetItem(str(i)))
            self.tbl_coords.setItem(i,1,QTableWidgetItem(str(i ** 2)))
            self.tbl_coords.setItem(i,2,QTableWidgetItem(str(i * 0.1)))


    def create_input_polynom_degree(self):
        self.lbl_polynom_degree = QLabel(self)
        self.lbl_polynom_degree.move(0, 185)
        self.lbl_polynom_degree.setText('Степень полинома:')
        self.lbl_polynom_degree.adjustSize()

        self.le_polynom_degree = QLineEdit(str(1), self)
        self.le_polynom_degree.move(0,215)

        validator = QRegExpValidator(QRegExp('[1-6]'))
        self.le_polynom_degree.setValidator(validator)


    def create_button_calc(self):
        self.btn_calc = QPushButton('Посчитать', self)
        self.btn_calc.move(0,245)
        self.btn_calc.clicked.connect(self.calc)     
        

    def create_about(self):
        self.lbl_about = QLabel(self)
        self.lbl_about.move(0, 360)
        self.lbl_about.setText('Лабораторная работа № 2. Автор: Г.Б. Ильин, ИУ7-78Б(В)')
        self.lbl_about.adjustSize()


    @staticmethod
    def show_error_message():
        msg = QErrorMessage()
        msg.showMessage('Неправильно введены числа!')
        msg.exec_()


    def read_cells(self, row): 
        row_values = []
        for col in range(3):
            cell_item = self.tbl_coords.item(row, col)

            if cell_item is not None:
                try:
                    row_values.append(float(cell_item.text()))
                except:
                    return None
            else:
                return None

        return row_values
    

    def calc(self):    
        try:
            inp=[]
            row_increment = functools.partial(next, itertools.count())
            
            while True:
                row_values = self.read_cells(row_increment())
                if row_values is None:
                    break
                inp.append(row_values)
            
            inp=np.array(inp)

            polynominal_degree=int(self.le_polynom_degree.text())
        except:
            self.show_error_message()
            return
   

        xs, ys = least_square_method.get_coords(inp)

        plt.plot(xs,ys)
        plt.scatter(xs, ys) 

        xs_for_approx, ys_by_coefs = least_square_method.lsm(inp, polynominal_degree)

        plt.plot(xs_for_approx, ys_by_coefs)
        plt.scatter(xs_for_approx, ys_by_coefs) 

        plt.show()



app = QApplication(sys.argv)
main_window = MyWindow()  
main_window.show()
app.exec_()
