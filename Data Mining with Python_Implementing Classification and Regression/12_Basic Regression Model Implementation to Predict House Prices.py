import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
# %matplotlib inline

# Loading dataset
dataset = pd.read_csv('input_data.csv')
print (len(dataset))
print (dataset.columns.values)

#split dataset
def split_data(dataset):
    square_feet_values = []
    price_values = []
    for square_feet, price in zip(dataset['square_feet'], dataset['price']):
        square_feet_values.append([square_feet])
        price_values.append(price)
    return square_feet_values, price_values

train_x, train_y = split_data(dataset)
print (train_x)
print (train_y)

#build simple regression model
regr = linear_model.LinearRegression()
regr.fit(train_x, train_y)

#fit the model
plt.scatter(train_x, train_y, color = 'blue')
plt.plot(train_x, regr.predict(train_x), color = 'red', linewidth = 4)
plt.show()

#predict price for 700sq
print(regr.predict(700))