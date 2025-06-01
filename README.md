# BiolabDatafileParsersApp

## About
BiolabDatafileParsersApp is a lightweight application for parsing data files generated in biology laboratories. The app currently supports the following input formats:

#### ABIF
ABIF is a format used by Applied Biosystems software. It is generated as a final output from sequencing instruments, including the Genetic Analyzer series. These files typically have .fsa and .ab1 extensions for fragment analysis and sequencing, respectively. ABIF is not UTF-8 encoded and cannot be read using plain text editors.

This app implements a parser that converts ABIF files into plain-text, tab-separated tables, enabling further data visualization using your preferred tools.

### Malvern PEAQ ITC
Software associated with Malvern PEAQ ITC instruments generates UTF-8 encoded data files with .itc and .apj extensions. These files can be opened in any text editor.
.itc files contain experimental setup and raw recorded data, and are relatively easy to manipulate.
.apj files contain processed data and are structured in XML format.

This app includes parsers that convert .itc and .apj files into plain-text, tab-separated tables for downstream visualization.

## Development
### Environment
Development was performed using conda 24.11.3 on a Linux distribution. The environment setup can be retrieved from the environment.yml file.
Alternatively, to manually set up the environment, install the following key libraries:
* `python=3.13.3`
* `pyqt=5.15.11`
* `matplotlib=3.10.3`

### Testing
The application has been tested on the following systems:
* Linux, miniconda
* Windows 10 Pro, Anaconda Prompt (conda version 25.3.1)

## Running

To launch the application, use the following command:

```bash
python main.py
```
or
```bash
python3 main.py
```

Note: It is recommended to use a conda environment. See the Development / Environment section above.

## Windows .exe

To share the app with Windows users, a standalone `.exe` file was generated using PyInstaller from a Conda environment in Windows.

#### Create a new environment that replicates the production setup:
```bash
conda create --name BiolabDatafileParsersApp --file environment.yml
conda activate BiolabDatafileParsersApp
```

#### Install PyInstaller and build the executable:
```bash
conda install -c conda-forge pyinstaller
pyinstaller --onefile --name BiolabDatafileParsers main.py
```

## Extending the App (Adding New Parsers)

To add a new parser to the application, you need to modify files in the `Parsers/` directory, specifically `Parsers/ParsersLib.py`.

#### Implement a parser in a python file.
Parsers must be single function with single input.
* Input : file_name (str)
* Output : a dictionnary with key (str) : value (str)
Place your script in `Parsers/`

#### Update ParsersLib.py
In the file `ParsersLib.py`, import your custom parser 
```python
from Parsers.MyCustomParser import MyCustomParser
```
Update the `PARSERS` variable. Add a key that describes your parser and map it to the parser function previously imported.

```python
PARSERS = {
  ...
  "Super parser for insane data" : MyCustomParser
}
```

(don't forget to add a comma at the end of the penultimate item in `PARSERS`)

#### Running main.py
While running `main.py`, those changes will result to the following behavior :
* A new parser will be able in parser selection. The new entry corresponds to the key in the `PARSERS` dict below (`"Super parser for insane data"`)
* If the parser run without raising any exception, the output will be splitted across multiple entries, following your parser output dict.
* keys of the output dict will build separated panels. The value of those keys is used as label for switching between panels.
* for each panel, the corresponding dict value (str) will be displayed
