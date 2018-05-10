########################################
# Information Gain Feature Selection
########################################

import math
from Training import feature, total_features


#Calculates the entropy of the given data set for the target attribute.
def entropy(data, target_attr):
    val_freq = {}
    data_entropy = 0.0
    # Calculate the frequency of each of the values in the target attr
    for record in data:
        if (val_freq.has_key(record[target_attr])):
            val_freq[record[target_attr]] += 1.0
        else:
            val_freq[record[target_attr]]  = 1.0
            
    # Calculate the entropy of the data for the target attribute
    for freq in val_freq.values():
        data_entropy += (-freq/len(data)) * math.log(freq/len(data), 2)   
    return data_entropy



# Calculates the information gain (reduction in entropy) that would result by splitting the data on the chosen attribute (attr).
#target_attr = last attribute which tells if there is an attack or no attack
def gain(data, attr, target_attr):
    val_freq = {}
    subset_entropy = 0.0

    # Calculate the frequency of each of the values in the target attribute
    for record in data:
        if (val_freq.has_key(record[attr])):
            val_freq[record[attr]] += 1.0
        else:
            val_freq[record[attr]]  = 1.0
          
    # Calculate the sum of the entropy for each subset of records weighted by their probability of occurence in the training set.
    for val in val_freq.keys():
        val_prob = val_freq[val] / sum(val_freq.values())
        data_subset = [record for record in data if record[attr] == val]
        subset_entropy += val_prob * entropy(data_subset, target_attr)
    # Subtract the entropy of the chosen attribute from the entropy of the whole data set with respect to the target attribute (and return it)
    return (entropy(data, target_attr) - subset_entropy)



def ig_list(traffic):
    gain_list=list()
    for j in range(total_features):
        gain_list.append(gain(traffic, j, 28))
    gain_dict = dict(zip(feature, gain_list))
    print("The Information Gain values are:")
    print(gain_dict)
    print("The sorted Information Gain values are:")
    sorted_gain_list = sorted(gain_dict, key = gain_dict.get)
    print(sorted_gain_list)
    return sorted_gain_list



def ent_list(traffic):
    ent_list=list()
    for i in range(total_features):
        ent_list.append(entropy(traffic,i))
    ent_dict = dict(zip(feature, ent_list))
    print("The entropy values are:")
    print(ent_dict)
    #Sort the entropy values
    print("The sorted entropy values are:")
    print(sorted(ent_dict, key = ent_dict.get))






