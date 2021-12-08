# read csv file
path = "/Users/folder"
with open(os.path.join(path, 'sub-fulder',"filename.csv"), 'r', encoding='UTF-8-sig') as data_file:

    csv_data = csv.reader(data_file, delimiter=',')
    next(csv_data, None) # skip one item(row) before your loop, simply call next(data, None)
    data = {} # dictionary

    for row in csv_data:
        # first column = key, second and third column = values
        data[row[0]] = (float(row[1]), float(row[2])) 

    return data
