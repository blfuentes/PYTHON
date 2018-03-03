from sklearn.datasets import load_iris
iris_dataset = load_iris()

# print(iris_dataset)

iris_x_features = iris_dataset.data
iris_y_target = iris_dataset.target

print(iris_x_features.shape)
print(iris_y_target.shape)

#split dataset into train and test data
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(iris_x_features, iris_y_target, test_size = 0.3)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

#knn classifier implementation
from sklearn.neighbors import KNeighborsClassifier
knn_classifier = KNeighborsClassifier(n_neighbors = 4)

knn_classifier.fit(x_train, y_train)
# predicting iris categories
# x_test = x_test.reshape(-1, 1)
print(knn_classifier.predict([x_test[0]]))
print(knn_classifier.predict([x_test[1]]))
print(knn_classifier.predict([x_test[2]]))
print(knn_classifier.predict([x_test[3]]))

# train accuracy
from sklearn import metrics
train_target_predictions = knn_classifier.predict(x_train)
print(metrics.accuracy_score(y_train, train_target_predictions))

#test accuracy
test_target_predictions = knn_classifier.predict(x_test)
print(metrics.accuracy_score(y_test, test_target_predictions))