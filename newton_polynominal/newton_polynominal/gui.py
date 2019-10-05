import sys
import functools
import itertools
from collections import OrderedDict
import math

from PyQt5.QtWidgets import QApplication, QMainWindow,  QPushButton,  QLabel, QErrorMessage, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import  QSize

from newton_polynominal import NewtonPolynominal


class MyWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)       
        self.setMinimumSize(QSize(600, 400))   

        self.create_table_params()
        self.create_table_xy()
        self.create_button_x_square()
        self.create_button_cos_x_minus_x()
        self.create_about()


    def create_table_params(self):
        self.tbl_params = QTableWidget(self)
        
        headers_horiz = ['Ввод']
        self.tbl_params.setColumnCount(len(headers_horiz))
        self.tbl_params.setHorizontalHeaderLabels(headers_horiz)

        headers_vert=["Координата","Значение", "Степ. полинома"]
        self.tbl_params.setRowCount(len(headers_vert))
        self.tbl_params.setVerticalHeaderLabels(headers_vert)

        self.tbl_params.setItem(0,0,QTableWidgetItem('x'))
        self.tbl_params.setItem(0,1,QTableWidgetItem('1.5'))
        self.tbl_params.setItem(0,2,QTableWidgetItem('3'))

        self.tbl_params.resize(200,140)

    def create_table_xy(self):
        self.tbl_xy = QTableWidget(self)

        headers_horiz = ["x", "y"]        
        self.tbl_xy.setColumnCount(len(headers_horiz))
        self.tbl_xy.setHorizontalHeaderLabels(headers_horiz)

        self.tbl_xy.setRowCount(10)

        #for example:
        self.tbl_xy.setItem(0,0,QTableWidgetItem('0.0'))
        self.tbl_xy.setItem(0,1,QTableWidgetItem('0.0'))

        self.tbl_xy.setItem(1,0,QTableWidgetItem('1.0'))
        self.tbl_xy.setItem(1,1,QTableWidgetItem('1.0'))

        self.tbl_xy.setItem(2,0,QTableWidgetItem('2.0'))
        self.tbl_xy.setItem(2,1,QTableWidgetItem('4.0'))
        
        self.tbl_xy.setItem(3,0,QTableWidgetItem('3.0'))
        self.tbl_xy.setItem(3,1,QTableWidgetItem('9.0'))
        
        self.tbl_xy.setItem(4,0,QTableWidgetItem('4.0'))
        self.tbl_xy.setItem(4,1,QTableWidgetItem('16.0'))

        self.tbl_xy.move(320, 0)
        self.tbl_xy.resize(250,340)


    def create_button_x_square(self):
        self.button_poly = QPushButton('y(x)=x^2', self)
        self.button_poly.move(0,215)
        self.button_poly.clicked.connect(self.button_x_square)  


    def create_button_cos_x_minus_x(self):
        self.button_poly_root = QPushButton('y(x)=cos(x)-x=0', self)
        self.button_poly_root.move(130,215)
        self.button_poly_root.clicked.connect(self.cos_x_minus_x)  


    def create_about(self):
        self.lbl_about = QLabel(self)
        self.lbl_about.move(0, 250)
        self.lbl_about.setText('Лабораторная работа № 1. Автор: Г.Б. Ильин, ИУ7-78Б(В)')
        self.lbl_about.adjustSize()


    @staticmethod
    def show_error_message():
        msg = QErrorMessage()
        msg.showMessage('Неправильно введены числа!')
        msg.exec_()

    
    @staticmethod
    def show_x_message(poly_result, fn_result):
        msg = QMessageBox(QMessageBox.Information,
            'Успех!',
            'Полином: {0:f}, \nФункция: {1:f}.'.format(poly_result, fn_result), 
            QMessageBox.Ok)
        msg.exec_() 

    @staticmethod
    def show_y_message(poly_result):
        msg = QMessageBox(QMessageBox.Information,
            'Успех!',
            'Корень: {0:f}'.format(poly_result), 
            QMessageBox.Ok)
        msg.exec_() 


    def button_x_square(self):
        self.calc_poly(lambda x: x**2 )


    def cos_x_minus_x(self):
        self.calc_poly(lambda x: math.cos(x)-x )


    def read_cells(self, row): 
        row_values = []
        for col in range(2):
            cell_item = self.tbl_xy.item(row, col)

            if cell_item is not None:
                try:
                    row_values.append(float(cell_item.text()))
                except:
                    return None
            else:
                return None

        return row_values


    def calc_poly(self, fn_for_check):
        try:
            y_by_x = OrderedDict()
            row = 0
            row_increment = functools.partial(next, itertools.count())

            while True:
                row_values = self.read_cells(row_increment())

                if row_values is None:
                    break
                else:
                    x,y = row_values
                    y_by_x[x] = y

            inputed_coord_name=self.tbl_params.item(0, 0).text()
            assert inputed_coord_name in ["x", "y"]

            inputed_value=float(self.tbl_params.item(1, 0).text())

            poly_degree=int(self.tbl_params.item(2, 0).text())

        except :
            self.show_error_message()
            return

        poly_result=NewtonPolynominal(y_by_x, inputed_coord_name, inputed_value, poly_degree).poly()
        #fn_result = inputed_value ** 2

        if inputed_coord_name=="x":
            fn_result=fn_for_check(inputed_value)
            self.show_x_message(poly_result, fn_result)
        else:
            self.show_y_message(poly_result)


app = QApplication(sys.argv)
main_window = MyWindow()  
main_window.show()
app.exec_()
