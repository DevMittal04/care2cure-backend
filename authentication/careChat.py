import numpy as np
import pandas as pd
import sklearn
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

states = ['Anxiety', 'Depression', 'Loneliness','Stress', 'Normal']

def ProcessChat(v):
    df = pd.read_csv("dataset.csv")
    df.head()
    
    X = df.iloc[:, :]
    le = LabelEncoder()
    X = df.apply(le.fit_transform)
    #OneHotEncoder().fit_transform(X).toarray()
    #X[X.columns[:-1]] = le.fit_transform(X[X.columns[:-1]])
    y = X["Disorder"]
    X.drop(X.columns[-1:], axis=1, inplace = True)
    X

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

    #print(X_train,y_train)
    clf = BernoulliNB()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print (accuracy_score(y_test, y_pred))
    w = X.iloc[5,:].values.reshape(1, -1)
    w = [v]
    #w = [[1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    arr = np.array(w)
    arr.reshape(-1, 1)
    #arr.values.reshape(1, -1)
    result = states[clf.predict(arr)[0]]
    print(result)
    return result