
import pandas as pd
import numpy as np
import pickle
import seaborn as sns
df = sns.load_dataset("iris")

X = np.array(df.iloc[:, 0:4])
y = np.array(df.iloc[:, 4:])

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.svm import SVC
sv = SVC(kernel='linear').fit(X_train,y_train)


pickle.dump(classifier, open('model.pkl','wb')) 
model=pickle.load(open("model.pkl", "rb"))
print(model.predict([[2, 3, 3,2]]))
