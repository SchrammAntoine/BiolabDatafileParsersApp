
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton

class RunButton(QWidget):
    """
    This Widget handle parser running.
    """
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        layout = QHBoxLayout()
        self.button = QPushButton("Run Parser")
        self.button.setFixedSize(100,50)
        self.button.clicked.connect(self.run_clicked)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def run_clicked(self) :
        try :
            self.parent.parse_file()
        except Exception :
            self.parent.push_error()