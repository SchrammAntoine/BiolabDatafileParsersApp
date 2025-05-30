
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QTextEdit, QLabel


class TextOutputBox(QWidget):
    """
    This Widget handle output text display
    """
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        layout = QVBoxLayout()

        self.parsing_result = {}
        self.freeze = False

        self.combo_box = QComboBox()
        self.combo_box.currentIndexChanged.connect(self.on_selection_change)
        layout.addWidget(self.combo_box)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        layout.addWidget(QLabel("Output:"))
        layout.addWidget(self.text_edit)
        self.setLayout(layout)

    def on_selection_change(self) :
        if self.freeze : return
        label = self.combo_box.currentText()
        text = self.parsing_result[label]
        self.text_edit.setPlainText(text)

    def set_parsing_result(self, parsing_result) :
        self.freeze = True
        self.parsing_result = parsing_result
        self.combo_box.clear()
        self.combo_box.addItems( parsing_result.keys() )
        self.combo_box.setCurrentIndex(0)
        self.freeze = False
        self.on_selection_change()

    def get_output(self):
        return self.text_edit.toPlainText()

    def get_label(self) :
        return self.combo_box.currentText()