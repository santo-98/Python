import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
Data = pd.read_csv("iris.csv", names=names)

array = Data.values

X = array[:,0:4]
y = array[:,-1]
X_train, X_validation, Y_train, Y_validation = train_test_split(X,y,test_size=0.20,random_state=1)

models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
names = []
results = [] 
for name, model in models:
	kfold = StratifiedKFold(n_splits=10,shuffle= True, random_state=1)
	cvresults = cross_val_score(model,X,y,cv=kfold,scoring='accuracy')
	results.append(cvresults.mean())
	names.append(name)
	print(cvresults)
	print('%s: %f (%f)' % (name, cvresults.mean(), cvresults.std()))