
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QFileDialog

class FileSelection(QWidget):
    """
    This Widget handle input file selection.
    """
    def __init__(self, parent):

        super().__init__()
        self.parent = parent
        self.selected_file_name = None
        layout = QHBoxLayout()

        self.button = QPushButton("Select File")
        self.button.setFixedSize(100,50)
        self.button.clicked.connect(self.open_file_dialog)
        self.label = QLabel("No file selected")

        layout.addWidget(self.button)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def open_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Data File", "", "All Files (*)")
        if file_name:
            self.label.setText(file_name)
            self.selected_file_name = file_name

    def get_filename(self) :
        return self.selected_file_name