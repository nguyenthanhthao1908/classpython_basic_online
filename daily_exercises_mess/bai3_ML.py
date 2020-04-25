from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


iris_dataset = load_iris()
X_train, X_test, Y_train, Y_test = train_test_split(iris_dataset.data, iris_dataset.target, random_state = 0)

model = DecisionTreeClassifier()
mymodel = model.fit(X_train, Y_train)

print(mymodel.score(X_test, Y_test))