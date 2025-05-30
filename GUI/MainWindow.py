
import sys
import os

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFileDialog

from GUI.Widget_FileSelection import FileSelection
from GUI.Widget_ParserSelection import ParserSelection
from GUI.Widget_Run import RunButton
from GUI.Widget_OutputDisplay import TextOutputBox
from GUI.Widget_SaveFile import SaveResultButton


class MainWindow(QWidget) :
    """
    Compile all widget together in a single window
    """
    def __init__(self, parser_list) :
        super().__init__()
        self.setWindowTitle("BioLab Data File Parser")
        layout = QVBoxLayout()

        self.file_selection = FileSelection(parent = self)
        self.parser_selection = ParserSelection(parent = self, parser_list=parser_list)
        self.run = RunButton(parent = self)
        self.output = TextOutputBox(parent = self)
        self.save = SaveResultButton(parent = self)

        layout.addWidget(self.file_selection)
        layout.addWidget(self.parser_selection)
        layout.addWidget(self.run)
        layout.addWidget(self.output)
        layout.addWidget(self.save)

        self.setLayout(layout)

    def parse_file(self) :
        file_name = self.file_selection.get_filename()
        Parser = self.parser_selection.get_parser()
        parsing_result = Parser(file_name)
        self.output.set_parsing_result(parsing_result)

    def save_output(self):

        ## Get text
        text = self.output.get_output()
        if text == "" : return

        ## Get input file
        input_file = self.file_selection.get_filename()
        if input_file is None: return

        ## Get Prefix
        prefix = self.output.get_label().replace(" ","_")
        if prefix == "ERROR" : return


        default_filename = os.path.splitext(os.path.basename(input_file))[0] + f"_{prefix}.txt"
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File As", default_filename, "Text Files (*.txt);;All Files (*)")
        if not file_path: return
        try:
            with open(file_path, "w") as f:
                f.write(text)
        except Exception as e:
            return

    def push_error(self) :
        error_output = {"ERROR" : "An error occurs.\nMake sure you are loading the correct file\nMake sure you are using the correct Parser"}
        self.output.set_parsing_result(error_output)


if __name__ == "__main__":
    main()
