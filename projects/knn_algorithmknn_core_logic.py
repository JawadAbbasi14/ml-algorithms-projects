import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv("dataset.csv")

x = data[['Math', 'English', 'CS' ]]
y = data["Career_Path"]

# Encode labels
object = LabelEncoder()
encoded_y = object.fit_transform(y)

# Train model
module = KNeighborsClassifier()
module.fit(x, encoded_y)

# Prediction
predicted = module.predict([[67, 67, 97]])
print("Your career path is:", object.inverse_transform(predicted))

