import pandas as pd
import numpy as np
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error


df = pd.read_csv("uber.csv")
df.head()


df.dtypes
df.describe()


# Remove unnecessary columns
df.drop(columns=["Unnamed: 0", "key"], errors="ignore", inplace=True)
# Remove missing values
df.dropna(inplace=True)


# Remove invalid fare and passenger values
df = df[(df["fare_amount"] > 0) &
         (df["passenger_count"] > 0) &
         (df["passenger_count"] <= 6)]

# Remove invalid NYC coordinates
df = df[df["pickup_latitude"].between(40, 42) &
        df["pickup_longitude"].between(-75, -72) &
        df["dropoff_latitude"].between(40, 42) &
        df["dropoff_longitude"].between(-75, -72)]

print(df.describe())



# Before removing outliers
print("Before removing outliers:", df.shape)

Q1 = df["fare_amount"].quantile(0.25)
Q3 = df["fare_amount"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

import matplotlib.pyplot as plt
sns.boxplot(x=df["fare_amount"])
plt.title("Outliers in Uber Fare")
plt.show()

# Remove outliers
df = df[df["fare_amount"].between(lower, upper)]

# After removing outliers
print("After removing outliers:", df.shape)





# Check correlation
print(df.corr(numeric_only=True)["fare_amount"].sort_values(ascending=False))




features = [
    "pickup_longitude", "pickup_latitude",
    "dropoff_longitude", "dropoff_latitude",
    "passenger_count"
]
X = df[features]

y = df["fare_amount"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)





lr = LinearRegression()

lr.fit(X_train, y_train)

y_pred_lr = lr.predict(X_test)

print("Linear Regression R2:",
      r2_score(y_test, y_pred_lr))




rf = RandomForestRegressor(n_estimators=50, random_state=42)

rf.fit(X_train, y_train)

y_pred_rf = rf.predict(X_test)

print("Random Forest R2:",
      r2_score(y_test, y_pred_rf))




print("Linear Regression RMSE:",
      np.sqrt(mean_squared_error(y_test, y_pred_lr)))

print("Random Forest RMSE:",
      np.sqrt(mean_squared_error(y_test, y_pred_rf)))



print("Actual fare:", y_test.values[:5])

print("Linear Regression prediction:", y_pred_lr[:5])

print("Random Forest prediction:", y_pred_rf[:5])