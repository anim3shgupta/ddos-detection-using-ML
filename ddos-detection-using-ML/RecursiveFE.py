######################################################
# Recursive Feature Elimination Feature Selection
######################################################
# Documentation: http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html

import pandas
from Training import filename_adj, feature
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE


def rfe():
    dataframe = pandas.read_csv(filename_adj, names=feature)
    array = dataframe.values
    X = array[:,0:28]
    Y = array[:,28]
    
    # feature extraction
    model = LogisticRegression()
    rfe = RFE(model, 1)
    fit = rfe.fit(X, Y)
    print("Num Features:", fit.n_features_)
    print("Selected Features:", fit.support_)
    print("Feature Ranking:", fit.ranking_)