import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# Read dataset
df = pd.read_csv("Churn_Modelling.csv")
df


df.drop(columns=["RowNumber", "CustomerId", "Surname"], errors="ignore", inplace=True)
df


# 2. Separate input features (X) from the target (y).
X = df.drop(columns=["Exited"]) ## 
y = df["Exited"]
# 3. Convert text categories into numeric columns using one-hot encoding.
X = pd.get_dummies(X, columns=["Geography", "Gender"], drop_first=True, dtype=int)


# 4. Split data: 80% for training and 20% for testing, preserving class proportions.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 5. Standardize features: learn scaling from training data and apply it to both sets.
scaler = StandardScaler() 
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# 6. Build and train a neural network with two hidden layers (16 and 8 neurons).
model = MLPClassifier(
    hidden_layer_sizes=(16, 8),
    activation="relu",
    solver="adam",
    max_iter=200,
    random_state=42
)
model.fit(X_train, y_train)


# 7. Predict test labels and evaluate the model.
predictions = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, predictions) * 100, 2), "%")
print("Confusion Matrix:\n", confusion_matrix(y_test, predictions))
print(classification_report(
    y_test,
    predictions,
    target_names=["Stayed (0)", "Exited (1)"],
    zero_division=0
))


# 8. Show the predicted churn probability for one test customer.
probability = model.predict_proba(X_test)[0][1]
actual = y_test.iloc[0]
predicted = predictions[0]
print("Churn probability:", round(probability * 100, 2), "%")
print("Prediction:", "CHURN" if predicted == 1 else "STAY")
print("Actual result:", "EXITED" if actual == 1 else "STAYED")