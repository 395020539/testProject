import sys
import time
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QProgressBar, QPushButton, QFileDialog, QHBoxLayout, QVBoxLayout, QMessageBox


class Worker(QThread):
    progress_changed = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self):
        for i in range(101):
            self.progress_changed.emit(i)
            time.sleep(0.05)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Selector")
        self.setFixedWidth(600)
        self.setFixedHeight(400)

        self.setWindowTitle("File Selector")

        self.file1_label = QLabel("File 1:")
        self.file1_path_label = QLabel("")
        self.file1_browse_button = QPushButton("Browse...")
        self.file1_browse_button.clicked.connect(self.browse_file1)

        self.file2_label = QLabel("File 2:")
        self.file2_path_label = QLabel("")
        self.file2_browse_button = QPushButton("Browse...")
        self.file2_browse_button.clicked.connect(self.browse_file2)

        self.progress_label = QLabel("Progress:")
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_process)

        file1_layout = QHBoxLayout()
        file1_layout.addWidget(self.file1_label)
        file1_layout.addWidget(self.file1_path_label)
        file1_layout.addWidget(self.file1_browse_button)

        file2_layout = QHBoxLayout()
        file2_layout.addWidget(self.file2_label)
        file2_layout.addWidget(self.file2_path_label)
        file2_layout.addWidget(self.file2_browse_button)

        progress_layout = QHBoxLayout()
        progress_layout.addWidget(self.progress_label)
        progress_layout.addWidget(self.progress_bar)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.start_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(file1_layout)
        main_layout.addLayout(file2_layout)
        main_layout.addLayout(progress_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        self.worker = Worker()
        self.worker.progress_changed.connect(self.progress_bar.setValue)

    def browse_file1(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File 1")
        if file_path:
            self.file1_path_label.setText(file_path)

    def browse_file2(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File 2")
        if file_path:
            self.file2_path_label.setText(file_path)

    def start_process(self):
        self.progress_bar.setValue(0)
        self.worker.start()
        self.start_button.setEnabled(False)
        self.worker.finished.connect(self.process_finished)

    def process_finished(self):
        self.start_button.setEnabled(True)
        self.progress_bar.setValue(100)
        QMessageBox.information(self, "Operation Complete", "Process finished.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = Example()
    example.show()
    sys.exit(app.exec_())
