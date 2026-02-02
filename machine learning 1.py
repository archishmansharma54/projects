import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
data= pd.read_csv("C:\\Users\\Sandeep Patra\\OneDrive\\Documents\\projects\\melb_data.csv")
y = data.Price
melbourne_features= ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt']
x = data[melbourne_features]
model=DecisionTreeRegressor(random_state=1)
model.fit(x,y)
# print(x.head()) 
# print(model.predict(x.head()))
# print(y.head())
# splitting data into training and validation data, for both features and target
# the split is based on a random number generator. Supplying a numeric value to random_state will always produce the same split.
train_x, val_x, train_y, val_y = train_test_split(x, y, random_state=0)
# defining the model
model=DecisionTreeRegressor()
# fitting the model
model.fit(train_x, train_y)
# making predictions on validation data
from sklearn.metrics import mean_absolute_error
val_predictions = model.predict(val_x)
print(mean_absolute_error(val_y, val_predictions))
