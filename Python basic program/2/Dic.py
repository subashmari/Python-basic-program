dict1 = {'StdNo':'032','StuName': 'Subash M', 'StuAge': 23, 'StuCity': 'Chennai', 'StuState': 'Tamil Nadu'}
print("\n Dictionary is :",dict1)
print("\n Student Name is :",dict1['StuName'])
print("\n Student City is :",dict1['StuCity'])
print("\n Student State is :",dict1['StuState'])
print("\n All Keys in Dictionary ")
for x in dict1:
 print(x)
print("\n All Values in Dictionary ")
for x in dict1:
 print(dict1[x])
dict1["Phno"]=9123599748
print("\n Updated Dictionary is :",dict1)
dict1["StuName"]="Black"
print("\n Updated Dictionary is :",dict1)
dict1.pop("StuAge");
print("\n Updated Dictionary is :",dict1)
print("Length of Dictionary is :",len(dict1))
dict2=dict1.copy()
print("\n New Dictionary is :",dict2)
dict1.clear()
print("\n Updated Dictionary is :",dict1)
