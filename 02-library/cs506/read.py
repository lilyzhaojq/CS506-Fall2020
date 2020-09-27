def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """

    res = []
    with open(csv_file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            list_of_string = line.split(",")

            list_of_values = []

            for item in list_of_string:
                try:
                    v = int(item)
                    list_of_values.append(v)

                except ValueError:
                    try:
                        v = float(item)
                        list_of_values.append(v)
                    
                    except ValueError:
                        v = item.strip(' " ')
                        list_of_values.append(v)
            res.append(list_of_values)

    return res





