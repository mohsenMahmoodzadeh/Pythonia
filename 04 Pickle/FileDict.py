import pickle
from collections.abc import MutableMapping


class FileDict():

   
    
    def __init__(self,name, dictionary={}):
        self.dictionary = dictionary
        self.data_name = name
        try:
            self.dictionary = FileDict.load(self, self.data_name)
            

        except:
            self.dictionary = dictionary

    
       
    def __getitem__(self, key):
        if key not in self.dictionary.keys():
            return None
        # if key == 'alaki':
        #     return None
        elif key == 'data_name':
            return None
        else:
            return self.dictionary[key]
    
    def __setitem__(self, key, value):
       
        if key == 'alaki':
           
            return None
        elif key == 'data_name':
            return None
        else:
            key_value = {key: value}
            key_value.update(self.dictionary)
            self.dictionary = key_value
            # FileDict.save(self, self.dictionary, self.data_name)
            

    def items(self):
        return self.dictionary.items()
       

    def __repr__(self):
        return repr(self.dictionary)

    def __del__(self):
        FileDict.save(self, self.dictionary, self.data_name)
        del self

    def save(self, dictionary, data_name):
        with open(data_name + '.pkl', 'wb') as f:
           
            pickle.dump(dictionary, f)
        f.close()

    def load(self, data_name):
        with open(str(data_name) + '.pkl', 'rb') as f:
            inst = pickle.load(f)
        f.close()        
        return inst
