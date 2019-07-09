from sklearn.datasets import load_digits

digits=load_digits()

data=digits.data
target=digits.target

imgs=digits.images

#print(imgs.shape)
#print(data.shape)

import cv2

ret,data=cv2.threshold(data,7,15,cv2.THRESH_BINARY)
ret,imgs=cv2.threshold(imgs,7,15,cv2.THRESH_BINARY)

from sklearn.svm import SVC

clsfr=SVC(kernel='linear')

clsfr.fit(data,target)

from sklearn.externals import joblib

joblib.dump(clsfr,'SVM_DIGITS_V1.sav')

#from matplotlib import pyplot as plt

#plt.imshow(imgs[1],cmap='binary')
#plt.show()
