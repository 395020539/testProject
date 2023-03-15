import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import threading

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.create_widgets()

    def create_widgets(self):
        # 选择文件按钮
        self.select_file_button = QPushButton("选择文件", self)
        self.select_file_button.clicked.connect(self.select_file)
        self.select_file_button.move(20, 20)

        # 文件路径显示
        self.file_path_label = QLabel("", self)
        self.file_path_label.move(120, 25)

        # 运算进度条
        self.progressbar = QProgressBar(self)
        self.progressbar.setGeometry(20, 60, 280, 20)

        # 运算按钮
        self.compute_button = QPushButton("开始运算", self)
        self.compute_button.clicked.connect(self.compute)
        self.compute_button.setGeometry(20, 100, 280, 30)
        self.compute_button.setEnabled(False)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "选择文件")
        if file_path:
            self.file_path_label.setText(file_path)
            self.compute_button.setEnabled(True)

    def compute(self):
        self.compute_button.setEnabled(False)
        file_path = self.file_path_label.text()

        # 加法运算，放在线程中执行，避免阻塞GUI线程
        def compute_task():
            sum = 0
            for i in range(1, 100):
                sum += i
                self.progressbar.setValue(i)
            QMessageBox.information(self, "运算完成", f"1到100的和为{sum}")
            self.compute_button.setEnabled(True)

        threading.Thread(target=compute_task).start()

if __name__ == '__main__':
    app = QApplication()
    example = App()
    example.show()
    sys.exit(app.exec_())
