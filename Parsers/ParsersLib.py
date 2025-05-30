
from Parsers.ABIF import ParseABIF
from Parsers.Malvern_PeaqItc_Itc import Parse_MalvernPeaqItc_Itc
from Parsers.Malvern_PeaqItc_Apj import Parse_MalvernPeaqItc_Apj


# For adding new parsers to the app, you are in the correct file.
# (1)   Implement a parser in a python file.
#       Parsers must be single function with single input.
#
#       Input : file_name (str)
#       Output : a dictionnary with key (str) : value (str)
#
# (2)   Place your script in this directory (BiolabDataParser_app/Parsers/)
#       In this file (ParsersLib.py), import your custom parser (from Parsers.MyCustomParser import MyCustomParser)
#       Update the PARSERS variable below. Add a key that describe your parser and map it to the parser function previously imported
#       exemple : "Super parser for insane data" : MyCustomParser
#       (don't forget to add a comma at the end of the penultimate item in PARSERS)
#
# (3)   While running main.py, those changes will result to the following behavior :
#           - A new parser will be able in parser selection. The new entry corresponds to the key in the PARSERS dict below ("Super parser for insane data")
#           - If the parser run without raising any exception, the output will be splitted across multiple entries, following your parser output dict.
#           - keys of the output dict will build separated panels. The value of those keys is used as label for switching between panels.
#           - for each panel, the corresponding dict value (str) will be displayed
#
# (4)   Running main.py from a terminal will instantly capture the changes. If you are using the app that way, your job terminates here.
#       For Windows deployement, I've opted for PyInstaller from a conda env.
#       If windows deployement matters, you need to re-generate the .exe from a Windows environment.

PARSERS = {
    "AppliedBiosystems_GeneticAnalyzer (*.fsa, *.ab1)" : ParseABIF,
    "Malvern_PEAQ-ITC_Experiment (*.itc)" : Parse_MalvernPeaqItc_Itc,
    "Malvern_PEAQ-ITC_Analysis (*.apj)" : Parse_MalvernPeaqItc_Apj
}