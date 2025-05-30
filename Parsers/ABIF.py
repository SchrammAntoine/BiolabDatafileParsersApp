from Parsers.ABIFReader import ABIFReader
import numpy as np
import sys

def ExtractProcessedSignals(reader) :
    header = """# Columns contain the following data
# (1) Frame #
# (2) Processed sigal on channel 1
# (3) Processed sigal on channel 2
# (4) Processed sigal on channel 3
# (5) Processed sigal on channel 4
"""

    try :
        intensities = np.array([
            reader.getData('DATA',9),
            reader.getData('DATA',10),
            reader.getData('DATA',11),
            reader.getData('DATA',12)
        ])
    except Exception :
        return ""

    table = list()
    for index, line in enumerate(intensities.T) :
        frame = index + 1
        line =  [
            str(frame),
            str(line[0]),
            str(line[1]),
            str(line[2]),
            str(line[3]),
        ]

        line = "\t".join(line)
        table.append(line)

    text = "\n".join(table)
    processed = header + text
    return processed

def ExtractRawSignal(reader) :
    header = """# Columns contain the following data
# (1) Frame #
# (2) Fluorescence Intensities on channel 1
# (3) Fluorescence Intensities on channel 2
# (4) Fluorescence Intensities on channel 3
# (5) Fluorescence Intensities on channel 4
# (6) This Frame in saturated
"""

    intensities = np.array([
        reader.getData('DATA',1),
        reader.getData('DATA',2),
        reader.getData('DATA',3),
        reader.getData('DATA',4)
    ])

    try :
        satd = reader.getData('Satd',1)
    except Exception :
        satd = []

    table = list()

    for index, line in enumerate(intensities.T) :

        frame = index + 1
        saturation = int(frame in satd)

        line =  [
            str(frame),
            str(line[0]),
            str(line[1]),
            str(line[2]),
            str(line[3]),
            str(saturation)
        ]

        line = "\t".join(line)
        table.append(line)

    text = "\n".join(table)
    row_signal = header + text
    return row_signal

def ExtractParameters(reader) :
    header = """# Columns contain the following data
# (1) Voltage, measured (decavolts)
# (2) Current, measured (milliAmps)
# (3) Power, measured (milliWatts)
# (4) Temperature, measured (degrees C)
"""

    parameters = np.array([
        reader.getData('DATA',5),
        reader.getData('DATA',6),
        reader.getData('DATA',7),
        reader.getData('DATA',8)
    ])

    table = list()
    for line in parameters.T :
        line = [ str(value) for value in line ]
        line = "\t".join(line)
        table.append(line)

    text = "\n".join(table)
    parameters = header + text
    return parameters

def ParseABIF(file_name) :

    reader = ABIFReader(file_name)

    raw_signal = ExtractRawSignal(reader)
    parameters = ExtractParameters(reader)
    processed = ExtractProcessedSignals(reader)
    reader.close()

    output = {
        "Raw Sigal" : raw_signal,
        "Parameters" : parameters,
        "Processed" : processed
    }
    return output

if __name__ == "__main__" :
    ParseABIF(sys.argv[1])
