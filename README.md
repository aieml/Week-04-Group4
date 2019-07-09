# Week-04-Group4
In this week we discussed about Support Vector Machine and we started the 2nd In Class Project.

## Code explanation

I have completed the ``` 4.0 GUI for Handwritten digits.py```, please check it. It gives good predictions. And also I have completed all the button functions.
A brief explanation is given for each function and other newly included code segments.

```python 
try:
    os.mkdir('data')
except:
    print('Path Already Exists')
```

This creates folder name "data" in the current working directory. This folder is used to save the images drawn in the canvas using the "save" button

```python 
from sklearn.externals import joblib
clsfr=joblib.load('SVM_DIGITS_V1.sav')
```

Loading the trained Support Vector Machine saved in the ```4.1 Digits dataset.py``` code

```python 
def save():

    global count
    
    img_array=np.array(img)
    img_array=cv2.resize(img_array,(8,8))

    path=os.path.join('data',str(count)+'.jpg')
    #path=data/0.jpg
    
    cv2.imwrite(path,img_array)

    count=count+1
```
Saves the image in "data" folder using the count, using the count variable (example 0.jpg)

```python 
def clear():

    global img,img_draw

    canvas.delete('all')
    img=Image.new('RGB',(width,height),(0,0,0))
    img_draw=ImageDraw.Draw(img)
    label_status.config(text='PREDICTED DIGIT: NONE')
```

Clear both the canvas and the image

```python 
def predict():
    
    img_array=np.array(img) #converting to numpy array
    img_array=cv2.cvtColor(img_array,cv2.COLOR_BGR2GRAY) #converting into a gray image
    img_array=cv2.resize(img_array,(8,8)) #resizing into 8x8

    #plt.imshow(img_array,cmap='binary')
    
    img_array=np.reshape(img_array,(1,64))  #reshaping into 1x64
    img_array=img_array/255.0*15.0

    result=clsfr.predict(img_array)

    label_status.config(text='PREDICTED DIGIT:'+str(result))
    
    plt.show()
```

Predicting the label. Note that we have do all the preprocessing operations that done to the training data to the testing data too.

```python 
def predict():
img=Image.new('RGB',(width,height),(0,0,0))
img_draw=ImageDraw.Draw(img)
```

Creating a pillow image object, since we cnnot convert the canvas into a numpy or any other compatiable version for opencv. 
