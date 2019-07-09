from sklearn.datasets.samples_generator import make_circles
import numpy as np

data,target=make_circles(100,factor=0.1,noise=0.1)

x=data[:,0]
y=data[:,1]

#z=3*np.power(x,2)+6*np.power(y,2)
z=np.exp(-(x*x+y*y))

new_data=[]

for i in range(0,len(target)):

    new_data.append([x[i],z[i]])

new_data=np.array(new_data)

from sklearn.model_selection import train_test_split

train_data,test_data,train_target,test_target=train_test_split(new_data,target,test_size=0.2)

from sklearn.svm import SVC

clsfr=SVC(kernel='linear')

#train the model
clsfr.fit(train_data,train_target)

result=clsfr.predict(test_data)

from sklearn.metrics import accuracy_score

accuracy=accuracy_score(test_target,result)

print('Accuracy:',accuracy)


from matplotlib import pyplot as plt

plt.scatter(x,z)
plt.show()
