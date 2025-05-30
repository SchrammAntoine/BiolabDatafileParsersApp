# BiolabDatafileParsersApp
A small app for parsing datafiles generated in Biology labs.

## Linux

### requirements

Development and testing has been performed in conda 24.11.3

* python=3.13.3
* pyqt=5.15.11
* matplotlib=3.10.3

### usage
`python3 main.py`


## Hack

For adding new parsers into the app, you must work in Parsers/ and Parsers/ParsersLib.py.

#### Implement a parser in a python file.
Parsers must be single function with single input.
* Input : file_name (str)
* Output : a dictionnary with key (str) : value (str)
Place your script in Parsers/

#### Update ParsersLib.py
In this file (`ParsersLib.py`), import your custom parser (`from Parsers.MyCustomParser import MyCustomParser`).
Update the `PARSERS` variable. Add a key that describes your parser and map it to the parser function previously imported.

exemple : `"Super parser for insane data" : MyCustomParser`

(don't forget to add a comma at the end of the penultimate item in `PARSERS`)

#### Running main.py
While running main.py, those changes will result to the following behavior :
* A new parser will be able in parser selection. The new entry corresponds to the key in the `PARSERS` dict below (`"Super parser for insane data"`)
* If the parser run without raising any exception, the output will be splitted across multiple entries, following your parser output dict.
* keys of the output dict will build separated panels. The value of those keys is used as label for switching between panels.
* for each panel, the corresponding dict value (str) will be displayed
Running main.py from a terminal will instantly capture the changes. If you are using the app that way, your job terminates here.

#### Windows Deployment
For Windows deployement, I've opted for PyInstaller from a conda env. If windows deployement matters, you need to re-generate the .exe from a Windows environment.
