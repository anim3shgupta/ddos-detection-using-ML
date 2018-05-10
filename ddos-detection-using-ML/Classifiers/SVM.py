######################
# SVM Classifier
######################


from Training import *
from sklearn.model_selection import KFold
from getAccuracy import getAccuracy
from sklearn import svm
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
import pandas, numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
import pickle


def svm(sorted_list, num_features):
    #Creating a list of the features based on the number of features to be selected
    selected_features = sorted_list[0:num_features]
    selected_features.append('attack?')
    print("Selected Features:")
    print(selected_features)
    
    #Reading the entire dataset
    dataframe = pandas.read_csv(filename_adj, names=feature)
    header_list = dataframe.columns.values
    
    #Preparing the subset of the dataset based on the selected features
    df_clax = pandas.DataFrame(columns=selected_features)
    for i in range(len(selected_features)):
        for j in range(len(header_list)):
            if(header_list[j]==selected_features[i]):
                df_clax[selected_features[i]] = dataframe[header_list[j]]
    array_clx = df_clax.values
    array_clx = array_clx[1:]
     
    #k-fold cross validation
    kf = KFold(n_splits=5) # Define the split - into 20 folds 
    sum = 0
    for train, test in kf.split(array_clx):
        train_data = np.array(array_clx)[train]
        test_data = np.array(array_clx)[test]
        train_data_part1 = []
        train_data_part2 = []
        test_data_part2 = []
        
        for packet in train_data:
            train_data_part1.append(packet[0:num_features])
            train_data_part2.append(packet[num_features])
        
        for packet in test_data:
            test_data_part2.append(packet[num_features])
        
        #Optimizing the parameters(C, gamma) of SVM and using those parameter values to fit the model
        C_range = np.logspace(-1, 10, 1)
        gamma_range = np.logspace(-1, 3, 1)
        param_grid = dict(gamma=gamma_range, C=C_range)
        model = GridSearchCV(SVC(), param_grid=param_grid)
        model.fit(train_data_part1,train_data_part2)
        testSet_values = []    
        
        for packet in test_data:
            testSet_values.append(packet[0:num_features])
        predictions = model.predict(testSet_values)
        accuracy = getAccuracy(test_data, predictions)
        sum += accuracy
    
    # Dump the trained decision tree classifier with Pickle
    SVM_pkl_filename = 'WRFS_SVM.pkl'
    # Open the file to save as pkl file
    SVM_model_pkl = open(SVM_pkl_filename, 'w')
    pickle.dump(model, SVM_model_pkl)
    # Close the pickle instances
    SVM_model_pkl.close()    
    
    #Find the average of the accuracy results
    average = sum/5
    print(average)
#     precision = precision_score(test_data_part2, predictions, average='macro')
# #     print(test_data_part2)
# #     print(predictions)
#     print("Precision: ", precision)
#     recall = recall_score(test_data_part2, predictions, average='macro')
    
#     print("Raw Actual Values: ", test_data_part2)
#     print("Length", len(test_data_part2))
#     for i in range(0, len(test_data_part2)):
#         if(test_data_part2[i] == 'normal.'):
#             test_data_part2[i] = 0
#         else:
#             test_data_part2[i] = 1
#     print("Actual Values in binary", test_data_part2)
#     print("Length", len(test_data_part2))
#     
#     
#     predictions = predictions.tolist()
#     print("Raw predictions: ", predictions)
#     print("Length", len(predictions))
#     for i in range(0, len(predictions)):
#         if(predictions[i] == 'normal.'):
#             predictions[i] = 0
#         else:
#             predictions[i] = 1
#     print("Predictions in binary", predictions)
#     print("Length", len(predictions))
    
    tn, fp, fn, tp = confusion_matrix(test_data_part2, predictions).ravel()
    print(tn)
    print(fp)
    print(fn)
    print(tp)
#     
#     
#     print("Recall: ", recall)
    return average