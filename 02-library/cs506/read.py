def convert_str(s):
    types = [int, float]
    for t in types:
        try:
            return t(s)
        except ValueError:
            pass
    return str(s).strip('\"')

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    res = []
    with open(csv_file_path, "r") as csv_file:
        lines = csv_file.readlines()
        for line in lines:
            row = []
            vals = line.strip("\n").split(",")
            for v in vals:
                row.append(convert_str(v))
            res.append(row)
    return res