###################################
# Weighted Ranked Feature Selection
###################################


from Training import feature

#Initialize an empty dictionary with keys from the feature list
WeightDict = dict.fromkeys(feature)
print(WeightDict)

sorted_gain_list = ['land', 'urgent', 'wrong_fragment', 'rerror_rate', 'srv_rerror_rate', 'count', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'duration', 'flag', 'serror_rate', 'srv_serror_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'diff_srv_rate', 'same_srv_rate', 'dst_host_same_srv_rate', 'srv_diff_host_rate', 'dst_host_diff_srv_rate', 'dst_host_srv_count', 'dst_host_srv_diff_host_rate', 'dst_host_count', 'protocol_type', 'srv_count', 'dst_host_same_src_port_rate', 'dst_bytes', 'service', 'src_bytes']
sorted_chi2_list  = ['dst_host_same_srv_rate', 'count', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'wrong_fragment', 'dst_host_rerror_rate', 'diff_srv_rate', 'dst_host_srv_rerror_rate', 'dst_host_diff_srv_rate', 'serror_rate', 'srv_serror_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'flag', 'dst_host_same_src_port_rate', 'protocol_type', 'srv_diff_host_rate', 'dst_host_srv_diff_host_rate', 'dst_host_srv_count', 'service', 'land', 'urgent', 'dst_host_count', 'srv_count', 'duration', 'src_bytes', 'dst_bytes']
sorted_rfe_list = ['diff_srv_rate', 'same_srv_rate', 'dst_host_srv_serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'protocol_type', 'dst_host_serror_rate', 'wrong_fragment', 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_same_srv_rate', 'dst_host_srv_rerror_rate', 'serror_rate', 'flag', 'dst_host_diff_srv_rate', 'count', 'service', 'dst_host_srv_count', 'srv_count', 'dst_host_rerror_rate', 'dst_host_count', 'src_bytes', 'srv_diff_host_rate', 'urgent', 'dst_bytes', 'land', 'duration']

sorted_gain_dict = {}
sorted_chi2_dict = {}
sorted_rfe_dict = {}

for i in range(0, len(sorted_gain_list)):
    sorted_gain_dict[sorted_gain_list[i]] = i
    sorted_chi2_dict[sorted_chi2_list[i]] = i
    sorted_rfe_dict[sorted_rfe_list[i]] = i
    
print("\n")
print(sorted_gain_dict)
print("\n")
print(sorted_chi2_dict)
print("\n")
print(sorted_rfe_dict)

for i in range(0, 28):
    WeightDict[feature[i]] = sorted_gain_dict[feature[i]] + sorted_chi2_dict[feature[i]] + sorted_rfe_dict[feature[i]]
    
print("\n")
print(WeightDict)

sorted_WRFS_list = []
sorted_WeightDict = sorted(WeightDict, key=WeightDict.get, reverse=True)

for r in sorted_WeightDict:
    print r, WeightDict[r]
    sorted_WRFS_list.append(r)
    
print("\n")
print(sorted_WRFS_list)
    


    