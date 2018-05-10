################################################
# Normalize the given file in the range of 0-1
################################################

import csv, sys

filename = 'kddcup.data_10_percent'

#Open the adjusted KDD dataset set and store it in a 2D list and normalize the list
def normalize(file_to_normalize):
    print("Normalizing data..")
    #Read the KDD CSV file
    with open(file_to_normalize, 'r') as f:
        file = csv.reader(f)
        traffic = []
        try:
            for packet in file:
                packet = packet[1:]
                traffic.append(packet)
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, file.line_num, e))
    f.close()
    #Normalizing the data
    
    data_min = 0
    data_max = 0
    
    for i in range(0, len(traffic)):
        for j in range(0,28):
            traffic[i][j] = float(traffic[i][j])
            if(traffic[i][j]<=data_min):
                data_min = traffic[i][j]
            if(traffic[i][j]>data_max):
                data_max = traffic[i][j]

    for i in range(0, len(traffic)):
        for j in range(0,28):
            traffic[i][j] = float(traffic[i][j])
            traffic[i][j] = ((traffic[i][j])-data_min)/(data_max-data_min)
#             traffic[i][j] = traffic[i][j] *1000
    
    print("Data Normalized.\n")
    return traffic