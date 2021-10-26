import os
import cv2 as cv
import numpy as np
from sklearn.model_selection import train_test_split , cross_val_score
from sklearn import tree, svm, decomposition
from sklearn.metrics import confusion_matrix, classification_report
from sklearn import tree
import pickle
 
    
def GenderClassifiyModelwithPCA():
    im_list = []
    for filename in os.listdir(f'E:/Dataset'):
        im = cv.imread(f'E:/Dataset/{filename}')
        im = cv.cvtColor(im, cv.COLOR_RGB2GRAY)
        im = cv.resize(im, (100,100))
        im_list.append(im)
        
    face_data = np.empty((len(im_list),100*100))
    i = 0
    for face in im_list:
        f = np.array(face).reshape((1,100*100))
        face_data[i] = f
        i += 1
    
    y = np.zeros(120)
    y[0:9] = 1
    y[10:19] = 2
    y[20:29] = 3
    y[30:39] = 4
    y[40:49] = 5
    y[50:59] = 6
    y[60:69] = 7
    y[70:79] = 8
    y[80:89] = 9
    y[90:99] = 10
    y[100:109] = 11
    y[110:119] = 12
            
    facepca = decomposition.PCA(n_components=54)
    facepca.fit(face_data, y)
    x_pca_train = facepca.transform(face_data)
    
    svmmodel = svm.SVC(kernel='linear')
    svmmodel.fit(x_pca_train, y)
    #modelpath = 'D:/backup05072564/Documents/AI2564'
    pickle.dump(svmmodel, open('E:/gendermodelpca.mol', 'wb'))
    pickle.dump(facepca, open('E:/gendermodelpca.pca', 'wb'))
    X_train, X_test, y_train, y_test = train_test_split(x_pca_train, y, test_size=0.4, random_state=0)
    modelSVM = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
    scores = cross_val_score(modelSVM, x_pca_train, y, cv=5)
    preDict =  modelSVM.predict(X_test)
    metrix = confusion_matrix(y_test,preDict)
    print(classification_report(y_test,preDict))
    print(scores)
    print(metrix)

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(x_pca_train,y)
    pickle.dump(clf, open('E:/gendermodelpcaTree.mol', 'wb'))
    pickle.dump(facepca, open('E:/gendermodelpcaTree.pca', 'wb'))

GenderClassifiyModelwithPCA()