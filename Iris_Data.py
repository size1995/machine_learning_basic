import numpy as np
import random
class DataSet():
    def __init__(self,data):
        self.dataset=np.array(data)
        self.data=self.dataset[:,:4]
        self.label=self.dataset[:,4:]
class Data_iris():
    def __init__(self,file_path):
        self.path=file_path
        self.dict= {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}
        self.data=self.load_data()
    def load_data(self):
        f = open(self.path)
        line = f.readline()
        data=[]
        while line:
            line=line.replace('\n','')
            line=line.split(",", 5)
            line[-1]=self.dict[line[-1]]
            line = list(map(float, line))
            line[-1]=int(line[-1])
            data.append(line)
            line = f.readline()
        f.close()
        return data
    def data_seperate(self,shuffle=True,test_rate=0.25):
        if shuffle:
            random.shuffle(self.data)
        data_num=len(self.data)
        test_num=int(data_num*test_rate)
        test_set=DataSet(self.data[:test_num])
        train_set=DataSet(self.data[test_num:])
        return train_set,test_set
