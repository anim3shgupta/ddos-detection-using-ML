


filename = 'kddcup.data_10_percent'
filename_adj = 'chopped_my_file'
# filename_adj = 'my_file'

feature = ['duration', 'protocol_type', 'service', 'flag','src_bytes','dst_bytes','land','wrong_fragment','urgent','count','srv_count','serror_rate','srv_serror_rate','rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate','srv_diff_host_rate'
,'dst_host_count','dst_host_srv_count','dst_host_same_srv_rate','dst_host_diff_srv_rate','dst_host_same_src_port_rate','dst_host_srv_diff_host_rate'
,'dst_host_serror_rate','dst_host_srv_serror_rate','dst_host_rerror_rate','dst_host_srv_rerror_rate', 'attack?']
total_features = (len(feature)-1)


import pandas
import random
import xlwt
from Normalize import normalize
import Classifiers.NaiveBayes
import  Classifiers.SVM
import Classifiers.DecisionTree
import Classifiers.RandomForest


def splitDataset(dataset, splitRatio):
    trainSize = int(len(dataset) * splitRatio)
    trainSet = []
    copy = dataset.tolist()
    while(len(trainSet)<trainSize):
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return [trainSet, copy]



def create_dataframe():
    dataframe = pandas.read_csv(filename_adj, names=feature)
    array = dataframe.values
    X = array[:,0:28]
    Y = array[:,28]
    return X,Y



def main():
    print("Starting application..\n")
    traffic = normalize(filename_adj)

    print("1 - Display the information gain list")
    print("2 - Display the Chi-squared list")
    print("3 - Display the Recursive Feature Elimination list")
    print("4 - Display the WRFS list")
    selection = input("Enter your selection: ")
    
    #########################
    #Information Gain list
    #########################
    if(selection == 1):
#         sorted_gain_list = InfoGain.ig_list(traffic)
        sorted_gain_list = ['land', 'urgent', 'wrong_fragment', 'rerror_rate', 'srv_rerror_rate', 'count', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'duration', 'flag', 'serror_rate', 'srv_serror_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'diff_srv_rate', 'same_srv_rate', 'dst_host_same_srv_rate', 'srv_diff_host_rate', 'dst_host_diff_srv_rate', 'dst_host_srv_count', 'dst_host_srv_diff_host_rate', 'dst_host_count', 'protocol_type', 'srv_count', 'dst_host_same_src_port_rate', 'dst_bytes', 'service', 'src_bytes']
        print("Features selected using Information Gain.")
    
    #########################
    #Chi-Squared list
    #########################
    elif(selection == 2):
#         sorted_chi2_list = Chi2.chi2_list()
        sorted_chi2_list  = ['dst_host_same_srv_rate', 'count', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'wrong_fragment', 'dst_host_rerror_rate', 'diff_srv_rate', 'dst_host_srv_rerror_rate', 'dst_host_diff_srv_rate', 'serror_rate', 'srv_serror_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'flag', 'dst_host_same_src_port_rate', 'protocol_type', 'srv_diff_host_rate', 'dst_host_srv_diff_host_rate', 'dst_host_srv_count', 'service', 'land', 'urgent', 'dst_host_count', 'srv_count', 'duration', 'src_bytes', 'dst_bytes']
        print("Features selected using Chi-squared.")
    
    ######################################
    #Recursive Feature Elimination list
    ######################################
    elif(selection == 3):
        sorted_rfe = ['diff_srv_rate', 'same_srv_rate', 'dst_host_srv_serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'protocol_type', 'dst_host_serror_rate', 'wrong_fragment', 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_same_srv_rate', 'dst_host_srv_rerror_rate', 'serror_rate', 'flag', 'dst_host_diff_srv_rate', 'count', 'service', 'dst_host_srv_count', 'srv_count', 'dst_host_rerror_rate', 'dst_host_count', 'src_bytes', 'srv_diff_host_rate', 'urgent', 'dst_bytes', 'land', 'duration']
        print("Features selected using Recursive Feature Elimination.")
        
    #########################
    #WRFS list
    #########################
    elif(selection == 4):
        sorted_WRFS_list = ['dst_bytes', 'src_bytes', 'srv_count', 'dst_host_count', 'service', 'duration', 'srv_diff_host_rate', 'dst_host_srv_count', 'dst_host_srv_diff_host_rate', 'dst_host_same_src_port_rate', 'urgent', 'land', 'protocol_type', 'dst_host_diff_srv_rate', 'flag', 'serror_rate', 'dst_host_rerror_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_same_srv_rate', 'dst_host_srv_rerror_rate', 'srv_serror_rate', 'count', 'diff_srv_rate', 'same_srv_rate', 'wrong_fragment', 'srv_rerror_rate', 'rerror_rate']
        print("Features selected using WRFS.")
    
    else:
        print("Invalid selection")
    
    print("\n")
    print("*****************")
    print("Classification")
    print("*****************")
    print("1 - Naive Bayes ")
    print("2 - SVM")
    print("3 - Decision Tree")
    print("4 - Random Forest")
    clx_selection = input("Enter your selection: ")
    
    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet("Sheet 1")
    sheet1.write(0, 2, "Accuracy Values")
    for i in range(4,5):
        num_features = i
        print("Number of features selected - ", i)
        
        ################
        #Naive Bayes
        ################
        if(selection == 1 and clx_selection == 1):
            print("Classifying using Naive Bayes...")
            accuracy =  Classifiers.NaiveBayes.naive_bayes(sorted_gain_list, num_features)
            sheet1.write(i, 2, accuracy)
        elif(selection == 2 and clx_selection == 1):
            print("Classifying using Naive Bayes...")
            accuracy = Classifiers.NaiveBayes.naive_bayes(sorted_chi2_list, num_features)
            sheet1.write(i, 5, accuracy)
        elif(selection == 3 and clx_selection == 1):
            print("Classifying using Naive Bayes...")
            accuracy = Classifiers.NaiveBayes.naive_bayes(sorted_rfe, num_features)
            sheet1.write(i, 2, accuracy)
        elif(selection == 4 and clx_selection == 1):
            print("Classifying using Naive Bayes...")
            accuracy = Classifiers.NaiveBayes.naive_bayes(sorted_WRFS_list, num_features)
            sheet1.write(i, 2, accuracy)
            
        ################
        #SVM
        ################
        elif(selection == 1 and clx_selection == 2):
            print("Classifying using SVM...")
            accuracy = Classifiers.SVM.svm(sorted_gain_list, num_features)
            sheet1.write(i, 3, accuracy)
        elif(selection == 2 and clx_selection == 2):
            print("Classifying using SVM...")
            accuracy = Classifiers.SVM.svm(sorted_chi2_list, num_features)
            sheet1.write(i, 3, accuracy)
        elif(selection == 3 and clx_selection == 2):
            print("Classifying using SVM...")
            accuracy = Classifiers.SVM.svm(sorted_rfe, num_features)
            sheet1.write(i, 3, accuracy)
        elif(selection == 4 and clx_selection == 2):
            print("Classifying using SVM...")
            accuracy = Classifiers.SVM.svm(sorted_WRFS_list, num_features)
            sheet1.write(i, 3, accuracy)
        
        ###################
        #Decision Trees
        ###################
        elif(selection == 1 and clx_selection == 3):
            print("Classifying using Decision Trees...")
            accuracy = Classifiers.DecisionTree.decision_tree(sorted_gain_list, num_features)
            sheet1.write(i, 3, accuracy)
        elif(selection == 2 and clx_selection == 3):
            print("Classifying using Decision Trees...")
            accuracy = Classifiers.DecisionTree.decision_tree(sorted_chi2_list, num_features)
            sheet1.write(i, 3, accuracy)
        elif(selection == 3 and clx_selection == 3):
            print("Classifying using Decision Trees...")
            accuracy = Classifiers.DecisionTree.decision_tree(sorted_rfe, num_features)
            sheet1.write(i, 3, accuracy)
        elif(selection == 4 and clx_selection == 3):
            print("Classifying using Decision Trees...")
            accuracy = Classifiers.DecisionTree.decision_tree(sorted_WRFS_list, num_features)
            sheet1.write(i, 3, accuracy)
        
        ################
        #Random Forest
        ################
        elif(selection == 1 and clx_selection == 4):
            print("Classifying using Random Forest...")
            accuracy = Classifiers.RandomForest.randomForest(sorted_gain_list, num_features)
            sheet1.write(i, 6, accuracy)
        elif(selection == 2 and clx_selection == 4):
            print("Classifying using Random Forest...")
            accuracy = Classifiers.RandomForest.randomForest(sorted_chi2_list, num_features)
            sheet1.write(i, 6, accuracy)
        elif(selection == 3 and clx_selection == 4):
            print("Classifying using Random Forest...")
            accuracy = Classifiers.RandomForest.randomForest(sorted_rfe, num_features)
            sheet1.write(i, 6, accuracy)
        elif(selection == 4 and clx_selection == 4):
            print("Classifying using Random Forest...")
            accuracy = Classifiers.RandomForest.randomForest(sorted_WRFS_list, num_features)
            sheet1.write(i, 6, accuracy)
        
        else:
            print("Invalid Selection")
        print("End")
        
    book.save("results.xls")

if __name__ == "__main__":
    main()
    

