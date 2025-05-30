
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox

class ParserSelection(QWidget):
    """
    This Widget handle parser selection.
    """
    def __init__(self, parent, parser_list):
        super().__init__()
        self.parent = parent
        self.parser_list = parser_list

        layout = QHBoxLayout()

        label = QLabel("Select Parser:")
        label.setMaximumWidth(label.sizeHint().width())
        layout.addWidget(label)

        self.combo_box = QComboBox()
        self.combo_box.addItems(parser_list.keys())
        self.combo_box.setMaxVisibleItems(10)

        layout.addWidget(self.combo_box)
        self.setLayout(layout)

    def get_parser(self):
        name = self.combo_box.currentText()
        Parser = self.parser_list[name]
        return Parser