import sys
import functools
import itertools

from PyQt5.QtWidgets import QApplication, QMainWindow,  QPushButton,  QLabel, QErrorMessage, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import  QSize

from newton_polynominal import NewtonPolynominal


class MyWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)       
        self.setMinimumSize(QSize(400, 300))   

        self.create_table()
        self.create_button_poly()
        self.create_button_poly_root()
        self.create_about()


    def create_table(self):
        self.tbl_input = QTableWidget(self)
        
        headers_horiz = ['Ввод']
        self.tbl_input.setColumnCount(len(headers_horiz))
        self.tbl_input.setHorizontalHeaderLabels(headers_horiz)

        headers_vert = ['x начальный (мин. -100)', 'x конечный (макс. 100)', 'шаги (один шаг = 0,1x)', 'степень полинома', 'x']
        self.tbl_input.setRowCount(len(headers_vert))
        self.tbl_input.setVerticalHeaderLabels(headers_vert)

        #
        self.tbl_input.setItem(0,0,QTableWidgetItem('0.0'))
        self.tbl_input.setItem(1,0,QTableWidgetItem('4.0'))
        self.tbl_input.setItem(2,0,QTableWidgetItem('10.0'))
        self.tbl_input.setItem(3,0,QTableWidgetItem('4'))
        self.tbl_input.setItem(4,0,QTableWidgetItem('1.5'))
        #

        self.tbl_input.resize(260,180)

    def create_button_poly(self):
        self.button_poly = QPushButton('y(x)=x^2', self)
        self.button_poly.move(0,215)
        self.button_poly.clicked.connect(self.calc_poly)  


    def create_button_poly_root(self):
        self.button_poly_root = QPushButton('y(x)=cos(x)-x=0', self)
        self.button_poly_root.move(130,215)
        
        #######!!!!!!!self.button_poly_root.clicked.connect(self.calc)


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
    def show_x_sqr_message(poly_result, fn_result):
        msg = QMessageBox(QMessageBox.Information,
            'Успех!',
            'Полином: {0:f}, \nФункция: {1:f}.'.format(poly_result, fn_result), 
            QMessageBox.Ok)
        msg.exec_() 


    def read_cell(self, row, left_border=sys.float_info.min, right_border=sys.float_info.max):
        cell_item = self.tbl_input.item(row, 0)
        result = float(cell_item.text()) if cell_item else 0.0

        #print(row, result, left_border, right_border)

        assert result >= left_border 
        assert result <= right_border

        return result


    def calc_poly(self):
        try:
            row_increment = functools.partial(next, itertools.count())

            x_0 = self.read_cell(row_increment(), - 100.0, 99.4)
            x_n = self.read_cell(row_increment(), x_0 + 0.06, 100.0)
            step = self.read_cell(row_increment(),1, 50)
            polynom_degree = self.read_cell(row_increment(), 2, 30)
            x = self.read_cell(row_increment(), -100.0, 100.0)
        except :
            self.show_error_message()
            return

        #poly_result=poly.poly(x_0, x_n, step, polynominal_degree, x)
        #fn_result=poly.fn_x_power_2(x)
        poly_result=NewtonPolynominal('x_power_2.csv', x_0, x_n, step, polynom_degree, x).poly()
        fn_result = x ** 2

        self.show_x_sqr_message(poly_result, fn_result)


app = QApplication(sys.argv)
main_window = MyWindow()  
main_window.show()
app.exec_()


input()