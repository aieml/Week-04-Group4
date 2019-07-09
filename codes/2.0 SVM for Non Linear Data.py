from sklearn.datasets.samples_generator import make_circles

data,target=make_circles(100,factor=0.1,noise=0.1)

from sklearn.model_selection import train_test_split

train_data,test_data,train_target,test_target=train_test_split(data,target,test_size=0.2)

from sklearn.svm import SVC

#clsfr=SVC(kernel='linear')
#clsfr=SVC(kernel='poly',degree=2)
clsfr=SVC(kernel='rbf')

#train the model
clsfr.fit(train_data,train_target)

result=clsfr.predict(test_data)

from sklearn.metrics import accuracy_score

accuracy=accuracy_score(test_target,result)

print('Accuracy:',accuracy)

from matplotlib import pyplot as plt

for i in range(0,len(target)):
    if(target[i]==0):
        plt.scatter(data[i,0],data[i,1],c='r')
    elif(target[i]==1):
        plt.scatter(data[i,0],data[i,1],c='b')

plt.show()


