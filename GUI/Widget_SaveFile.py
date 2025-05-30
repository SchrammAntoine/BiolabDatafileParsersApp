
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton


class SaveResultButton(QWidget):
    """
    This Widget handle output save to file (txt)
    """
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        layout = QHBoxLayout()
        self.button = QPushButton("Save Output")
        self.button.setFixedSize(100,50)
        self.button.clicked.connect(self.save_button_clicked)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def save_button_clicked(self) :
        self.parent.save_output()
