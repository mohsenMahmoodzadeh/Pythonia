from FileDict import FileDict
import pickle


# try:
#     with open('person1.pkl', 'rb') as f:
#         # print(f)
#         inst = pickle.load(f)
#         print(inst)
# except OSError as err:
#     print('error number= ' + str(err.errno))

# data = pickle.load('person1.pkl')
# print(data)

data = FileDict('person1')

data['name'] = 'mohsen'
data['family'] = 'mahmoodzadeh'
# data['alaki'] = 'foo'

print(data['alaki'])
print(data)







# color = {'lion': 'yellow', 'tiger': 'red'}

# f = open('save.pkl', 'wb')
# pickle.dump(color, f)

# f = open('save.pkl', 'rb')
# load = pickle.load(f)
# print(load)
# help(load)

''' object = Class()
    object.method()'''
''' Class.method(object)'''

