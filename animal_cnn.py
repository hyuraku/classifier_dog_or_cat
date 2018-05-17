from keras.models import Sequential
from keras.layers import Convolution2D,MaxPooling2D
from keras.layers import Activation,Dropout,Flatten,Dense
from keras.utils import  np_utils
import numpy as np

classes=["dog","cat"]
num_classes=len(classes)
image_size=50

def normal(x):
    return x.astype("float")/256

# メインの関数を定義
def main():
    X_train,X_test,y_train,y_test=np.load("./animal.npy")
    X_train=normal(X_train)
    X_test=normal(X_test)
    y_train=np_utils.to_categorical(y_train,num_classes)
    y_test=np_utils.to_categorical(y_test,num_classes)

    model=model_train(X_train,y_train)
    model_eval(model,X_test,y_test)
