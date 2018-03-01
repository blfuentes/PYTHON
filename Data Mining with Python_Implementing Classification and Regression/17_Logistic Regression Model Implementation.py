import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics

anes_dataset = pd.read_csv('anes_dataset.csv')

print ("Number of observations: ", anes_dataset.shape[0])
print ("Number of features: ", anes_dataset.shape[1])

print ("Features: ", anes_dataset.columns.values)

print(anes_dataset.describe())

headers = list(anes_dataset.columns.values)
features = headers[:-1]
target = headers[-1]
print ("Features: ", features)
print ("Target: ", target)

x_train, x_test, y_train, y_test = train_test_split(anes_dataset[features], anes_dataset[target], test_size = 0.4)
print ("x_train shape: ", x_train.shape)
print ("y_train shape: ", y_train.shape)
print ("x_test shape: ", x_test.shape)
print ("y_test shape: ", y_test.shape)

#logistic regression model with 4 features
features_4 = ['TVnews', 'age', 'educ', 'income']
model_with_4_features = LogisticRegression()
model_with_4_features.fit(x_train[features_4], y_train)

train_accuracy = model_with_4_features.score(x_train[features_4], y_train)
print ("Train accuracy: ", train_accuracy)

#logistic regression model with all features
model_with_all_features = LogisticRegression()
model_with_all_features.fit(x_train, y_train)
train_accuracy = model_with_all_features.score(x_train, y_train)
print ("Train accuracy: ", train_accuracy)

#prediction with both the models
test_observation1_for_4_features_model = x_test[features_4][:1]
print (test_observation1_for_4_features_model)

test_observation1_for_all_features_model  = x_test[:1]
print (test_observation1_for_all_features_model)

print (model_with_4_features.predict(test_observation1_for_4_features_model))
print (model_with_all_features.predict(test_observation1_for_all_features_model))

#accuracies
model_with_4_features_prediction = model_with_4_features.predict(x_test[features_4])
model_with_4_features_test_accuracy = metrics.accuracy_score(y_test, model_with_4_features_prediction)
model_with_all_features_prediction = model_with_all_features.predict(x_test)
model_with_all_features_test_accuracy = metrics.accuracy_score(y_test, model_with_all_features_prediction)

print ("Model with 4 features test accuracy: ", model_with_4_features_test_accuracy)
print ("Model with all features test accuracy: ", model_with_all_features_test_accuracy)


