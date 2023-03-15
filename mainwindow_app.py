# -*- coding: utf-8 -*-


from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget
from PySide6.QtCore import Qt
from MainWindow_demo import Ui_MainWindow
from PySide6.QtWidgets import *
from form_demo import Ui_Formdemo

class MyWindow(QMainWindow, Ui_Formdemo):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.retranslateUi(self)

        # self.pushButton.clicked.connect(self.hello)
        self.btntest.clicked.connect(self.select_file_mech)
        self.pushButton.clicked.connect(self.select_file_geskon)
        self.pushButton_2.clicked.connect(self.select_file_dcm)
        self.pushButton_3.clicked.connect(self.select_file_a2l)
        self.pushButton_4.clicked.connect(self.select_file_data)



    def hello(self):
        print("hello")

    def select_file_mech(self):
        file_path_mech, _ = QFileDialog.getOpenFileName(self, "选择文件")
        if file_path_mech:
            # self.file_path_label.setText(file_path_mech)
            self.lineEdit.setText(file_path_mech)
            # self.compute_button.setEnabled(True)

    def select_file_geskon(self):
        file_path_geskon, _ = QFileDialog.getOpenFileName(self, "选择文件")
        if file_path_geskon:
            self.lineEdit_2.setText(file_path_geskon)

    def select_file_dcm(self):
        file_path_dcm, _ = QFileDialog.getOpenFileName(self, "选择文件")
        if file_path_dcm:
            self.lineEdit_3.setText(file_path_dcm)

    def select_file_a2l(self):
        file_path_a2l, _ = QFileDialog.getOpenFileName(self, "选择文件")
        if file_path_a2l:
            self.lineEdit_4.setText(file_path_a2l)

    def select_file_data(self):
        file_path_data, _ = QFileDialog.getOpenFileName(self, "选择文件")
        if file_path_data:
            self.lineEdit_5.setText(file_path_data)



if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()