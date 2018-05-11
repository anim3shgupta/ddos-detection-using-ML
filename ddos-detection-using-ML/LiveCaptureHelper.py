'''
Created on Apr 3, 2018

@author: animesh
'''
from LiveCapture import *

sorted_IG_list = ['land', 'urgent', 'wrong_fragment', 'rerror_rate', 'srv_rerror_rate', 'count', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'duration', 'flag', 'serror_rate', 'srv_serror_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'diff_srv_rate', 'same_srv_rate', 'dst_host_same_srv_rate', 'srv_diff_host_rate', 'dst_host_diff_srv_rate', 'dst_host_srv_count', 'dst_host_srv_diff_host_rate', 'dst_host_count', 'protocol_type', 'srv_count', 'dst_host_same_src_port_rate', 'dst_bytes', 'service', 'src_bytes']
sorted_Chi2_list  = ['dst_host_same_srv_rate', 'count', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'wrong_fragment', 'dst_host_rerror_rate', 'diff_srv_rate', 'dst_host_srv_rerror_rate', 'dst_host_diff_srv_rate', 'serror_rate', 'srv_serror_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'flag', 'dst_host_same_src_port_rate', 'protocol_type', 'srv_diff_host_rate', 'dst_host_srv_diff_host_rate', 'dst_host_srv_count', 'service', 'land', 'urgent', 'dst_host_count', 'srv_count', 'duration', 'src_bytes', 'dst_bytes']
sorted_rfe = ['diff_srv_rate', 'same_srv_rate', 'dst_host_srv_serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'protocol_type', 'dst_host_serror_rate', 'wrong_fragment', 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_same_srv_rate', 'dst_host_srv_rerror_rate', 'serror_rate', 'flag', 'dst_host_diff_srv_rate', 'count', 'service', 'dst_host_srv_count', 'srv_count', 'dst_host_rerror_rate', 'dst_host_count', 'src_bytes', 'srv_diff_host_rate', 'urgent', 'dst_bytes', 'land', 'duration']
sorted_WRFS_list = ['dst_bytes', 'src_bytes', 'srv_count', 'dst_host_count', 'service', 'duration', 'srv_diff_host_rate', 'dst_host_srv_count', 'dst_host_srv_diff_host_rate', 'dst_host_same_src_port_rate', 'urgent', 'land', 'protocol_type', 'dst_host_diff_srv_rate', 'flag', 'serror_rate', 'dst_host_rerror_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_same_srv_rate', 'dst_host_srv_rerror_rate', 'srv_serror_rate', 'count', 'diff_srv_rate', 'same_srv_rate', 'wrong_fragment', 'srv_rerror_rate', 'rerror_rate']


def IG_NB(window_dataframe):
    header_list = window_dataframe.columns.values
    NumFeatures = 24
    selected_features = sorted_IG_list[0:NumFeatures]
    #Preparing the subset of the live window based on the selected features
    df_clax = pandas.DataFrame(columns=selected_features)
    for i in range(len(selected_features)):
        for j in range(len(header_list)):
            if(header_list[j]==selected_features[i]):
                df_clax[selected_features[i]] = window_dataframe[header_list[j]]
    window_array = df_clax.values
    # Loading the saved pickle
    model_pkl = open('./Pickles/IG_NB.pkl', 'rb')
    model = pickle.load(model_pkl)
    
    testSet_values = window_array.tolist()
    predictions = (model.predict(testSet_values)).tolist()
    
    #Categorizing windows as attack windows or normal windows
    normal_packets = 0
    attack_packets = 0
    for value in predictions:
        if(value == 'normal.'):
            normal_packets = normal_packets + 1
        else:
            attack_packets = attack_packets + 1
    if (attack_packets >= 50):
        print("Attack Window")
        predictions = ['attack']
    else:
        print("Normal Window")
        predictions = ['normal']
    return (predictions)
    
def IG_SVM(window_dataframe):
    header_list = window_dataframe.columns.values
    NumFeatures = 23
    selected_features = sorted_IG_list[0:NumFeatures]
    #Preparing the subset of the live window based on the selected features
    df_clax = pandas.DataFrame(columns=selected_features)
    for i in range(len(selected_features)):
        for j in range(len(header_list)):
            if(header_list[j]==selected_features[i]):
                df_clax[selected_features[i]] = window_dataframe[header_list[j]]
    window_array = df_clax.values
    # Loading the saved pickle
    model_pkl = open('./Pickles/IG_SVM.pkl', 'rb')
    model = pickle.load(model_pkl)
    
    testSet_values = window_array.tolist()
    predictions = (model.predict(testSet_values)).tolist()
    
    #Categorizing windows as attack windows or normal windows
    normal_packets = 0
    attack_packets = 0
    for value in predictions:
        if(value == 'normal.'):
            normal_packets = normal_packets + 1
        else:
            attack_packets = attack_packets + 1
    if (attack_packets >= 50):
        print("Attack Window")
        predictions = ['attack']
    else:
        print("Normal Window")
        predictions = ['normal']
    return (predictions)
    
def IG_DT(window_dataframe):
    header_list = window_dataframe.columns.values
    NumFeatures = 23
    selected_features = sorted_IG_list[0:NumFeatures]
    #Preparing the subset of the live window based on the selected features
    df_clax = pandas.DataFrame(columns=selected_features)
    for i in range(len(selected_features)):
        for j in range(len(header_list)):
            if(header_list[j]==selected_features[i]):
                df_clax[selected_features[i]] = window_dataframe[header_list[j]]
    window_array = df_clax.values
    # Loading the saved pickle
    model_pkl = open('./Pickles/IG_DT.pkl', 'rb')
    model = pickle.load(model_pkl)
    
    testSet_values = window_array.tolist()
    predictions = (model.predict(testSet_values)).tolist()

    #Categorizing windows as attack windows or normal windows
    normal_packets = 0
    attack_packets = 0
    for value in predictions:
        if(value == 'normal.'):
            normal_packets = normal_packets + 1
        else:
            attack_packets = attack_packets + 1
    if (attack_packets >= 50):
        print("Attack Window")
        predictions = ['attack']
    else:
        print("Normal Window")
        predictions = ['normal']
    return (predictions)
    
def IG_RF(window_dataframe):
    header_list = window_dataframe.columns.values
    NumFeatures = 23
    selected_features = sorted_IG_list[0:NumFeatures]
    #Preparing the subset of the live window based on the selected features
    df_clax = pandas.DataFrame(columns=selected_features)
    for i in range(len(selected_features)):
        for j in range(len(header_list)):
            if(header_list[j]==selected_features[i]):
                df_clax[selected_features[i]] = window_dataframe[header_list[j]]
    window_array = df_clax.values
    # Loading the saved pickle
    model_pkl = open('./Pickles/IG_RF.pkl', 'rb')
    model = pickle.load(model_pkl)
    
    testSet_values = window_array.tolist()
    predictions = (model.predict(testSet_values)).tolist()
    
    #Categorizing windows as attack windows or normal windows
    normal_packets = 0
    attack_packets = 0
    for value in predictions:
        if(value == 'normal.'):
            normal_packets = normal_packets + 1
        else:
            attack_packets = attack_packets + 1
    if (attack_packets >= 50):
        print("Attack Window")
        predictions = ['attack']
    else:
        print("Normal Window")
        predictions = ['normal']
    return (predictions)

def Chi2_NB(window_dataframe):
    header_list = window_dataframe.columns.values
    NumFeatures = 25
    selected_features = sorted_Chi2_list[0:NumFeatures]
    #Preparing the subset of the live window based on the selected features
    df_clax = pandas.DataFrame(columns=selected_features)
    for i in range(len(selected_features)):
        for j in range(len(header_list)):
            if(header_list[j]==selected_features[i]):
                df_clax[selected_features[i]] = window_dataframe[header_list[j]]
    window_array = df_clax.values
    # Loading the saved pickle
    model_pkl = open('./Pickles/Chi2_NB.pkl', 'rb')
    model = pickle.load(model_pkl)
    
    testSet_values = window_array.tolist()
    predictions = (model.predict(testSet_values)).tolist()
    
    #Categorizing windows as attack windows or normal windows
    normal_packets = 0
    attack_packets = 0
    for value in predictions:
        if(value == 'normal.'):
            normal_packets = normal_packets + 1
        else:
            attack_packets = attack_packets + 1
    if (attack_packets >= 50):
        print("Attack Window")
        predictions = ['attack']
    else:
        print("Normal Window")
        predictions = ['normal']
    return (predictions)

def Chi2_SVM(window_dataframe):
    header_list = window_dataframe.columns.values
    NumFeatures = 17
    selected_features = sorted_Chi2_list[0:NumFeatures]
    #Preparing the subset of the live window based on the selected features
    df_clax = pandas.DataFrame(columns=selected_features)
    for i in range(len(selected_features)):
        for j in range(len(header_list)):
            if(header_list[j]==selected_features[i]):
                df_clax[selected_features[i]] = window_dataframe[header_list[j]]
    window_array = df_clax.values
    # Loading the saved pickle
    model_pkl = open('./Pickles/Chi2_SVM.pkl', 'rb')
    model = pickle.load(model_pkl)
    
    testSet_values = window_array.tolist()
    predictions = (model.predict(testSet_values)).tolist()
    
    #Categorizing windows as attack windows or normal windows
    normal_packets = 0
    attack_packets = 0
    for value in predictions:
        if(value == 'normal.'):
            normal_packets = normal_packets + 1
        else:
            attack_packets = attack_packets + 1
    if (attack_packets >= 50):
        print("Attack Window")
        predictions = ['attack']
    else:
        print("Normal Window")
        predictions = ['normal']
    return (predictions)

def Chi2_DT(window_dataframe):
    header_list = window_dataframe.columns.values
    NumFeatures = 16
    selected_features = sorted_Chi2_list[0:NumFeatures]
    #Preparing the subset of the live window based on the selected features
    df_clax = pandas.DataFrame(columns=selected_features)
    for i in range(len(selected_features)):
        for j in range(len(header_list)):
            if(header_list[j]==selected_features[i]):
                df_clax[selected_features[i]] = window_dataframe[header_list[j]]
    window_array = df_clax.values
    # Loading the saved pickle
    model_pkl = open('./Pickles/Chi2_DT.pkl', 'rb')
    model = pickle.load(model_pkl)
    
    testSet_values = window_array.tolist()
    predictions = (model.predict(testSet_values)).tolist()
    
    #Categorizing windows as attack windows or normal windows
    normal_packets = 0
    attack_packets = 0
    for value in predictions:
        if(value == 'normal.'):
            normal_packets = normal_packets + 1
        else:
            attack_packets = attack_packets + 1
    if (attack_packets >= 50):
        print("Attack Window")
        predictions = ['attack']
    else:
        print("Normal Window")
        predictions = ['normal']
    return (predictions)

def Chi2_RF(window_dataframe):
    header_list = window_dataframe.columns.values
    NumFeatures = 16
    selected_features = sorted_Chi2_list[0:NumFeatures]
    #Preparing the subset of the live window based on the selected features
    df_clax = pandas.DataFrame(columns=selected_features)
    for i in range(len(selected_features)):
        for j in range(len(header_list)):
            if(header_list[j]==selected_features[i]):
                df_clax[selected_features[i]] = window_dataframe[header_list[j]]
    window_array = df_clax.values
    # Loading the saved pickle
    model_pkl = open('./Pickles/Chi2_RF.pkl', 'rb')
    model = pickle.load(model_pkl)
    
    testSet_values = window_array.tolist()
    predictions = (model.predict(testSet_values)).tolist()
    
    #Categorizing windows as attack windows or normal windows
    normal_packets = 0
    attack_packets = 0
    for value in predictions:
        if(value == 'normal.'):
            normal_packets = normal_packets + 1
        else:
            attack_packets = attack_packets + 1
    if (attack_packets >= 50):
        print("Attack Window")
        predictions = ['attack']
    else:
        print("Normal Window")
        predictions = ['normal']
    return (predictions)



def RFE_NB(window_dataframe):
    header_list = window_dataframe.columns.values
    NumFeatures = 20
    selected_features = sorted_rfe[0:NumFeatures]
    #Preparing the subset of the live window based on the selected features
    df_clax = pandas.DataFrame(columns=selected_features)
    for i in range(len(selected_features)):
        for j in range(len(header_list)):
            if(header_list[j]==selected_features[i]):
                df_clax[selected_features[i]] = window_dataframe[header_list[j]]
    window_array = df_clax.values
    # Loading the saved pickle
    model_pkl = open('./Pickles/RFE_NB.pkl', 'rb')
    model = pickle.load(model_pkl)
    
    testSet_values = window_array.tolist()
    predictions = (model.predict(testSet_values)).tolist()
    
    #Categorizing windows as attack windows or normal windows
    normal_packets = 0
    attack_packets = 0
    for value in predictions:
        if(value == 'normal.'):
            normal_packets = normal_packets + 1
        else:
            attack_packets = attack_packets + 1
    if (attack_packets >= 50):
        print("Attack Window")
        predictions = ['attack']
    else:
        print("Normal Window")
        predictions = ['normal']
    return (predictions)
    
def RFE_SVM(window_dataframe):
    header_list = window_dataframe.columns.values
    NumFeatures = 7
    selected_features = sorted_rfe[0:NumFeatures]
    #Preparing the subset of the live window based on the selected features
    df_clax = pandas.DataFrame(columns=selected_features)
    for i in range(len(selected_features)):
        for j in range(len(header_list)):
            if(header_list[j]==selected_features[i]):
                df_clax[selected_features[i]] = window_dataframe[header_list[j]]
    window_array = df_clax.values
    # Loading the saved pickle
    model_pkl = open('./Pickles/RFE_SVM.pkl', 'rb')
    model = pickle.load(model_pkl)
    
    testSet_values = window_array.tolist()
    predictions = (model.predict(testSet_values)).tolist()
    
    #Categorizing windows as attack windows or normal windows
    normal_packets = 0
    attack_packets = 0
    for value in predictions:
        if(value == 'normal.'):
            normal_packets = normal_packets + 1
        else:
            attack_packets = attack_packets + 1
    if (attack_packets >= 50):
        print("Attack Window")
        predictions = ['attack']
    else:
        print("Normal Window")
        predictions = ['normal']
    return (predictions)

def RFE_DT(window_dataframe):
    header_list = window_dataframe.columns.values
    NumFeatures = 11
    selected_features = sorted_rfe[0:NumFeatures]
    #Preparing the subset of the live window based on the selected features
    df_clax = pandas.DataFrame(columns=selected_features)
    for i in range(len(selected_features)):
        for j in range(len(header_list)):
            if(header_list[j]==selected_features[i]):
                df_clax[selected_features[i]] = window_dataframe[header_list[j]]
    window_array = df_clax.values
    # Loading the saved pickle
    model_pkl = open('./Pickles/RFE_DT.pkl', 'rb')
    model = pickle.load(model_pkl)
    
    testSet_values = window_array.tolist()
    predictions = (model.predict(testSet_values)).tolist()
    
    #Categorizing windows as attack windows or normal windows
    normal_packets = 0
    attack_packets = 0
    for value in predictions:
        if(value == 'normal.'):
            normal_packets = normal_packets + 1
        else:
            attack_packets = attack_packets + 1
    if (attack_packets >= 50):
        print("Attack Window")
        predictions = ['attack']
    else:
        print("Normal Window")
        predictions = ['normal']
    return (predictions)

def RFE_RF(window_dataframe):
    header_list = window_dataframe.columns.values
    NumFeatures = 11
    selected_features = sorted_rfe[0:NumFeatures]
    #Preparing the subset of the live window based on the selected features
    df_clax = pandas.DataFrame(columns=selected_features)
    for i in range(len(selected_features)):
        for j in range(len(header_list)):
            if(header_list[j]==selected_features[i]):
                df_clax[selected_features[i]] = window_dataframe[header_list[j]]
    window_array = df_clax.values
    # Loading the saved pickle
    model_pkl = open('./Pickles/RFE_RF.pkl', 'rb')
    model = pickle.load(model_pkl)
    
    testSet_values = window_array.tolist()
    predictions = (model.predict(testSet_values)).tolist()
    
    #Categorizing windows as attack windows or normal windows
    normal_packets = 0
    attack_packets = 0
    for value in predictions:
        if(value == 'normal.'):
            normal_packets = normal_packets + 1
        else:
            attack_packets = attack_packets + 1
    if (attack_packets >= 50):
        print("Attack Window")
        predictions = ['attack']
    else:
        print("Normal Window")
        predictions = ['normal']
    return (predictions)

def WRFS_NB(window_dataframe):
    header_list = window_dataframe.columns.values
    NumFeatures = 8
    selected_features = sorted_WRFS_list[0:NumFeatures]
    #Preparing the subset of the live window based on the selected features
    df_clax = pandas.DataFrame(columns=selected_features)
    for i in range(len(selected_features)):
        for j in range(len(header_list)):
            if(header_list[j]==selected_features[i]):
                df_clax[selected_features[i]] = window_dataframe[header_list[j]]
    window_array = df_clax.values
    # Loading the saved pickle
    model_pkl = open('./Pickles/WRFS_NB.pkl', 'rb')
    model = pickle.load(model_pkl)
    
    testSet_values = window_array.tolist()
    predictions = (model.predict(testSet_values)).tolist()
    
    #Categorizing windows as attack windows or normal windows
    normal_packets = 0
    attack_packets = 0
    for value in predictions:
        if(value == 'normal.'):
            normal_packets = normal_packets + 1
        else:
            attack_packets = attack_packets + 1
    if (attack_packets >= 50):
        print("Attack Window")
        predictions = ['attack']
    else:
        print("Normal Window")
        predictions = ['normal']
    return (predictions)

def WRFS_SVM(window_dataframe):
    header_list = window_dataframe.columns.values
    NumFeatures = 4
    selected_features = sorted_WRFS_list[0:NumFeatures]
    #Preparing the subset of the live window based on the selected features
    df_clax = pandas.DataFrame(columns=selected_features)
    for i in range(len(selected_features)):
        for j in range(len(header_list)):
            if(header_list[j]==selected_features[i]):
                df_clax[selected_features[i]] = window_dataframe[header_list[j]]
    window_array = df_clax.values
    # Loading the saved pickle
    model_pkl = open('./Pickles/WRFS_SVM.pkl', 'rb')
    model = pickle.load(model_pkl)
    
    testSet_values = window_array.tolist()
    predictions = (model.predict(testSet_values)).tolist()
    
    #Categorizing windows as attack windows or normal windows
    normal_packets = 0
    attack_packets = 0
    for value in predictions:
        if(value == 'normal.'):
            normal_packets = normal_packets + 1
        else:
            attack_packets = attack_packets + 1
    if (attack_packets >= 50):
        print("Attack Window")
        predictions = ['attack']
    else:
        print("Normal Window")
        predictions = ['normal']
    return (predictions)

def WRFS_DT(window_dataframe):
    header_list = window_dataframe.columns.values
    NumFeatures = 4
    selected_features = sorted_WRFS_list[0:NumFeatures]
    #Preparing the subset of the live window based on the selected features
    df_clax = pandas.DataFrame(columns=selected_features)
    for i in range(len(selected_features)):
        for j in range(len(header_list)):
            if(header_list[j]==selected_features[i]):
                df_clax[selected_features[i]] = window_dataframe[header_list[j]]
    window_array = df_clax.values
    # Loading the saved pickle
    model_pkl = open('./Pickles/WRFS_DT.pkl', 'rb')
    model = pickle.load(model_pkl)
    
    testSet_values = window_array.tolist()
    predictions = (model.predict(testSet_values)).tolist()
    
    #Categorizing windows as attack windows or normal windows
    normal_packets = 0
    attack_packets = 0
    for value in predictions:
        if(value == 'normal.'):
            normal_packets = normal_packets + 1
        else:
            attack_packets = attack_packets + 1
    if (attack_packets >= 50):
        print("Attack Window")
        predictions = ['attack']
    else:
        print("Normal Window")
        predictions = ['normal']
    return (predictions)

def WRFS_RF(window_dataframe):
    header_list = window_dataframe.columns.values
    NumFeatures = 5
    selected_features = sorted_WRFS_list[0:NumFeatures]
    #Preparing the subset of the live window based on the selected features
    df_clax = pandas.DataFrame(columns=selected_features)
    for i in range(len(selected_features)):
        for j in range(len(header_list)):
            if(header_list[j]==selected_features[i]):
                df_clax[selected_features[i]] = window_dataframe[header_list[j]]
    window_array = df_clax.values
    # Loading the saved pickle
    model_pkl = open('./Pickles/WRFS_RF.pkl', 'rb')
    model = pickle.load(model_pkl)
    
    testSet_values = window_array.tolist()
    predictions = (model.predict(testSet_values)).tolist()
    
    #Categorizing windows as attack windows or normal windows
    normal_packets = 0
    attack_packets = 0
    for value in predictions:
        if(value == 'normal.'):
            normal_packets = normal_packets + 1
        else:
            attack_packets = attack_packets + 1
    if (attack_packets >= 50):
        print("Attack Window")
        predictions = ['attack']
    else:
        print("Normal Window")
        predictions = ['normal']
    return (predictions)


    
