import sys
import functools
import itertools

import numpy as np
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QApplication, QMainWindow,  QPushButton,  QLabel, QErrorMessage, QMessageBox, QTableWidget, QTableWidgetItem, QLineEdit
from PyQt5.QtCore import  QSize, QRegExp
from PyQt5.QtGui import QRegExpValidator

import runge_kutta_electricity


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


        ROWS_COUNT = 7

        self.tbl_input = QTableWidget(self)

        headers_horiz = ["Название", "Обозначение", "Ед. изм.", "Значение"]
        self.tbl_input.setColumnCount(len(headers_horiz))
        self.tbl_input.setHorizontalHeaderLabels(headers_horiz)

        self.tbl_input.setRowCount(ROWS_COUNT)

        self.tbl_input.move(120, 0)
        self.tbl_input.resize(430,300)

        row_increment = functools.partial(next, itertools.count())

        input_row(row_increment(), "Сопротивление", "R", "Ом", 0.5)
        input_row(row_increment(), "Индуктивность", "L", "Генри", 60e-6)
        input_row(row_increment(), "Ёмкость", "C", "Фарад", 150e-6)
        input_row(row_increment(), "Нач. ток", "I_0", "Ампер", 0)
        input_row(row_increment(), "ЭДС", "E", "Вольт", 1500)
        input_row(row_increment(), "Нач. напряжение", "U_0", "Вольт", 1500)
        input_row(row_increment(), "Шаг", "h", "Секунд", 1e-6)


    def create_button_calc(self):
        self.btn_calc = QPushButton('Посчитать', self)
        self.btn_calc.move(0,245)
        self.btn_calc.clicked.connect(self.calc)


    def create_about(self):
        self.lbl_about = QLabel(self)
        self.lbl_about.move(0, 360)
        self.lbl_about.setText('Лабораторная работа № 4. Автор: Г.Б. Ильин, ИУ7-78Б(В)')
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
        times=[]
        ICs=[]
        UCs=[]

        try:
            row_increment = functools.partial(next, itertools.count())

            times, ICs, UCs = runge_kutta_electricity.rke(
                R=self.read_cells(row_increment()),
                L=self.read_cells(row_increment()),
                C=self.read_cells(row_increment()),
                IC0=self.read_cells(row_increment()),
                E=self.read_cells(row_increment()),
                UC0=self.read_cells(row_increment()),
                h=self.read_cells(row_increment()),
            )

        except:
            self.show_error_message()
            return


        plt.plot(times,ICs)
        plt.scatter(times, ICs)
        plt.ylabel("Ток - ампер")
        plt.xlabel("Время - секунд")
        plt.show()

        plt.plot(times,UCs)
        plt.scatter(times, UCs)
        plt.ylabel("Напряжение - вольт")
        plt.xlabel("Время - секунд")
        plt.show()




app = QApplication(sys.argv)
main_window = MyWindow()
main_window.show()
app.exec_()
