import numpy as np
from PIL import Image
import os,glob
from sklearn import model_selection

classes=["dog","cat"]
num_classes=len(classes)
image_size=50

#画像読み込み

X=[]
Y=[]

for index,classlabel in enumerate(classes):
    photos_dir="./"+classlabel
    files=glob.glob(photos_dir + "/*.jpg")
    for i ,file enumerate(files):
        if i >320: break
        image=Image.open(file)
        image=image.convert("RGB")
        image=image.resize((image_size,image_size))
        data=np.asarray(image)
        X.append(data)
        Y.append(index)

X = np.array(X)
Y = np.array(Y)

X_train,X_test,y_train,y_test=model_selection.train_test_split(X,Y)
xy=(X_train,X_test,y_train,y_test)
np.save("./animal.npy",xy)
