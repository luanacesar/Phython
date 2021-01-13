# Dictionaries can be retrieved by key name
my_dict = {'key1':'value1', 'key2': 'value2'}
print(my_dict)
print(my_dict['key1'])

products = {'apple':2.99, 'oranges': 1.99, 'milk':5.8}
print(products['oranges'])

d ={'k1':123,'k2':[0,1,2],'k3':{'insidekey':100}}
print(d['k2'])
print(d['k3']['insidekey'])

d ={ 'k1':100, 'k2':200}
d.update({'k3':300})
print(d)
d.update({'k1':'new'})
print(d)

print(d.keys())
print(d.values())