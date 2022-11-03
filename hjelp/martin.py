headerLine = dataFile.readline()

headerLine = headerLine.strip("\n")

headerLine = headerLine.split(";")

x_label = headerLine[0]
y_label = headerLine[1]