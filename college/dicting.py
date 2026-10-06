dict1={"name": "rakshit","age": 18,"class":"FYBSC DSBA"},{"name":"adity","age":19,"class":"FYBSC DSBA"}
# dict_keys=dict.keys(dict1)
# dict_values=dict.values(dict1)
# dict_items=dict.items(dict1)
# print(dict_keys,dict_values,dict_items)

print(list(map(lambda x: x["name"],dict1)))

print(list(filter(lambda x: x["name"]=="rakshit",dict1)))


a=[1,25,7,3,7,2,53,79,3,462,12,155,868,5,3]
print(list(filter(lambda x: x%2==0,a)))
