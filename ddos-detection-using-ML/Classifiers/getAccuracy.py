##########################
# Calculate Accuracy
##########################

def getAccuracy(testSet, predictions):
    correct = 0
    for packet in range(len(testSet)):
        if testSet[packet][-1] == predictions[packet]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0