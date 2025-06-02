
import sys
import xml.etree.ElementTree as ET
import numpy as np

def FetchRawSignal(experiments) :
    data_points = experiments.find("DataPoints")
    raw_time_serie = [ float(item.get("T")) for item in data_points ]
    raw_dp_serie =  [ float(item.get("DP")) for item in data_points ]
    raw_temperature_serie =  [ float(item.get("Tmp")) for item in data_points ]

    text = [f"{time}\t{dp}\t{temp}" for time, dp,temp in zip(raw_time_serie, raw_dp_serie, raw_temperature_serie)]


    header = """# Columns contain the following data
# (1) time (sec)
# (2) DP (cal/mol)
# (3) Temperature (°C)
"""
    return header+"\n".join(text)



def FetchBaseline(experiments) :
    baseline = experiments.find("Baseline").find("BaselinePoints")
    time_serie = np.array([ float(item.get("T")) for item in baseline ])
    dp_serie = np.array([ float(item.get("DP")) for item in baseline ])
    temp_serie = np.array([ float(item.get("Tmp")) for item in baseline ])

    text = [f"{time}\t{dp}\t{temp}" for time, dp,temp in zip(time_serie, dp_serie, temp_serie)]
    header = """# Columns contain the following data
# (1) time (sec)
# (2) Baseline DP (cal/mol)
# (3) Temperature (°C)
"""
    return header+"\n".join(text)


def FetchAnalysis(experiments) :
    injections = experiments.find("Injections").findall('Injection')
    indices = np.array([int(injection.find("Index").text) for injection in injections ])
    XD_s = np.array([ float(injection.find("XD").text) for injection in injections ])
    MD_s = np.array([ float(injection.find("MD").text) for injection in injections ]) ## This is the molar ratio
    XMT_s = np.array([ float(injection.find("XMT").text) for injection in injections ])
    DH_s = np.array([ float(injection.find("DH").text) for injection in injections ])
    DHControlSubtracted_s = np.array([ float(injection.find("DHControlSubtracted").text) for injection in injections ])
    NDH_s = np.array([ float(injection.find("NDH").text) for injection in injections ]) ## This is integrated heat, in cal/mol.

    text = [
        f"{XD}\t{MD}\t{XMT}\t{DH}\t{DHControlSubtracted}\t{NDH}"
        for XD,MD,XMT,DH,DHControlSubtracted,NDH in zip(XD_s,MD_s,XMT_s,DH_s,DHControlSubtracted_s,NDH_s)
    ]

    header = """# Columns contain the following data
# (1) XD
# (2) MD 
# (3) XMT : molar ratio
# (4) DH
# (5) DHControlSubtracted
# (6) NDH : integrated heat in cal/mol
"""
    return header+"\n".join(text)


def FetchModelParam(experiments) :

    fitting_model = experiments.find("FittingModel").text

    fitting_params = experiments.find("FittingResult")
    if fitting_model == "_2Sites" :
        fit_params = {
            "model" : "_2Sites",
            "N1" : fitting_params.find("N1").text,
            "Kd1" : fitting_params.find("Kd1").text,
            "DH1" : fitting_params.find("DH1").text,
            "N2" : fitting_params.find("N2").text,
            "Kd2" : fitting_params.find("Kd2").text,
            "DH2" : fitting_params.find("DH2").text,
            "DG1" : fitting_params.find("DG1").text,
            "DG2" : fitting_params.find("DG2").text,
            "TDS1" : fitting_params.find("TDS1").text,
            "TDS2" : fitting_params.find("TDS2").text
        }

    if fitting_model == "_1Site_Competitive" :
        fit_params = {
            "model" : "_1Site_Competitive",
            "N" : float(fitting_params.find("N").text),
            "Kd" : float(fitting_params.find("Kd").text),
            "DH" : float(fitting_params.find("DH").text),
            "DG" : float(fitting_params.find("DG").text),
            "DS" : float(fitting_params.find("DS").text)
        }


    text = [f"{label} : {value}" for label, value in fit_params.items()]
    return "\n".join(text)

def FetchFit(experiments) :
    fitting = experiments.find("FittingResult").find('FitPoints')
    fit_x = np.array([ float(item.find("X").text) for item in fitting ])
    fit_y = np.array([ float(item.find("Y").text) for item in fitting ]) ## This is expected heat, according to model, given in kcal/mol

    lines = [ f"{x}\t{y}" for x,y in zip(fit_x, fit_y) ]
    return '\n'.join(lines)


def Parse_MalvernPeaqItc_Apj(file_name) :
    tree = ET.parse(file_name)
    root = tree.getroot()
    experiments = root.find("Experiments").find("Experiment")


    raw_signal = FetchRawSignal(experiments)
    baseline = FetchBaseline(experiments)
    analysis = FetchAnalysis(experiments)
    model_param = FetchModelParam(experiments)
    fit = FetchFit(experiments)

    output = {
        "Raw Signal" : raw_signal,
        "Baseline" : baseline,
        "Integrated Signal" : analysis,
        "Fit" : fit,
        "Model Parameters" : model_param
    }
    return output


if __name__ == "__main__" :
    Parse_MalvernPeaqItc_Apj(sys.argv[1])
