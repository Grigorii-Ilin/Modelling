import sys
import functools
import itertools

import numpy as np

from PyQt5.QtWidgets import QApplication, QMainWindow,  QPushButton,  QLabel, QErrorMessage, QMessageBox, QTableWidget, QTableWidgetItem, QLineEdit
from PyQt5.QtCore import  QSize

from data_getter import Data
import temperature_calc


class MyWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(600, 400))

        self.create_table_input()
        self.create_button_calc()
        self.create_about()


    def create_table_input(self):
        def input_row(row_index, name, literal, measure, value):
            self.tbl_input.setItem(row_index, 0, QTableWidgetItem(name))
            self.tbl_input.setItem(row_index, 1, QTableWidgetItem(literal))
            self.tbl_input.setItem(row_index, 2, QTableWidgetItem(measure))
            self.tbl_input.setItem(row_index, 3, QTableWidgetItem(str(value)))


        ROWS_COUNT = 9

        self.tbl_input = QTableWidget(self)

        headers_horiz = ["Название", "Обозначение", "Ед. изм.", "Значение"]
        self.tbl_input.setColumnCount(len(headers_horiz))
        self.tbl_input.setHorizontalHeaderLabels(headers_horiz)

        self.tbl_input.setRowCount(ROWS_COUNT)

        self.tbl_input.move(120, 0)
        self.tbl_input.resize(430,300)

        row_increment = functools.partial(next, itertools.count())

        input_row(row_increment(), "Длина сержня", "L", "см", 10)
        input_row(row_increment(), "Радиус стержня", "R", "см", 0.5)
        input_row(row_increment(), "Окр. темп-ра", "Te", "Кельвин", 300)
        input_row(row_increment(), "Внешний поток", "F", "В/(см2*К)", 100)
        input_row(row_increment(), "Коэф. теплопров. нач", "k0", "В/(см*К)", 0.1)
        input_row(row_increment(), "Коэф. теплопров. кон", "kN", "В/(см*К)", 0.05)
        input_row(row_increment(), "Коэф. теплоотд. нач.", "α0", "В/(см2*К)", 10e-2)
        input_row(row_increment(), "Коэф. теплоотд. кон.", "αN", "В/(см2*К)", 0.5e-2)
        input_row(row_increment(), "Шаг", "h", "см", 1e-2)


    def create_button_calc(self):
        self.btn_calc = QPushButton('Посчитать', self)
        self.btn_calc.move(0,245)
        self.btn_calc.clicked.connect(self.calc)


    def create_about(self):
        self.lbl_about = QLabel(self)
        self.lbl_about.move(0, 360)
        self.lbl_about.setText('Лабораторная работа № 5. Автор: Г.Б. Ильин, ИУ7-78Б(В)')
        self.lbl_about.adjustSize()


    @staticmethod
    def show_error_message():
        msg = QErrorMessage()
        msg.showMessage('Неправильно введены числа!')
        msg.exec_()


    def read_cells(self, row):
        cell_item = self.tbl_input.item(row, 3)
        result = float(cell_item.text())
        return result



    def calc(self):
        try:
            row_increment = functools.partial(next, itertools.count())

            data= Data(
                l=self.read_cells(row_increment()),
                R=self.read_cells(row_increment()),
                Te=self.read_cells(row_increment()),
                F0=self.read_cells(row_increment()),
                k0=self.read_cells(row_increment()),
                kN=self.read_cells(row_increment()),
                alpha0=self.read_cells(row_increment()),
                alphaN=self.read_cells(row_increment()),
                h=self.read_cells(row_increment())
                )

        except:
            self.show_error_message()
            return

        temperature_calc.main_proc(data)


app = QApplication(sys.argv)
main_window = MyWindow()
main_window.show()
app.exec_()
