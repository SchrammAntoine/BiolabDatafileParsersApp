
import sys

def Parse_MalvernPeaqItc_Itc(file_name) :
    f = open(file_name)
    data = list()
    titration_index = None
    for line in f :
        line = line.strip()
        if line.startswith("@") :
            titration_index = line[1:].split(',')[0]
            continue
        if titration_index is None :
            continue
        line = line.replace(",","\t")
        line = str(titration_index) + "\t" + line
        data.append(line)
    header = """# Columns contain the following data
# (1) Injection #
# (2) time
# (3) DP
# (4) Temperature
# (5) unknown
# (6) unknown (temperature like)
# (7) unknown
# (8) unknown
# (9) unknown (DP like)
# (10) unknown (DP like)

"""
    raw_signal = header + "\n".join(data)
    
    output = {
        "Raw Signal" : raw_signal
    }
    return output

if __name__ == "__main__" :
    Parse_MalvernPeaqItc_Itc(sys.argv[1])
