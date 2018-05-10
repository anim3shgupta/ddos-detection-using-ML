###################################
# Chi-Squared Feature Selection
###################################

from Training import filename_adj, feature
import pandas
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import numpy as np

def chi2_list():
    dataframe = pandas.read_csv(filename_adj, names=feature)
    #array = dataframe.values
    #X = dataframe.iloc[:,0:28]
    #Y = dataframe.iloc[:,28]
    array = dataframe.values
    X = array[:,0:28]
    Y = array[:,28]
    # feature extraction
    test = SelectKBest(score_func=chi2, k=10)
    fit = test.fit(X,Y)
    chi2_list = fit.scores_
    chi2_dict = dict(zip(feature, chi2_list))
    print("The chi-squared values are: ")
    # summarize scores
    np.set_printoptions(precision=3)
    print(chi2_dict)
    print("The sorted chi-squared values are: ")
    sorted_chi2_list = sorted(chi2_dict, key = chi2_dict.get)
    print(sorted_chi2_list)
    return sorted_chi2_list
