import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)


# 1. Load dataset
df = pd.read_csv("emails.csv")

# 2. Preprocessing
df.drop("Email No.", axis=1, inplace=True)

df.dropna(inplace=True)



# 3. Separate features and target
X = df.drop("Prediction", axis=1)
y = df["Prediction"]

# 4. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)



# 5. KNN Classification
knn = KNeighborsClassifier()

knn.fit(X_train, y_train)

y_pred_knn = knn.predict(X_test)

print("KNN Accuracy:", accuracy_score(y_test, y_pred_knn))

print("KNN Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_knn))

print("KNN Classification Report:")
print(classification_report(y_test, y_pred_knn))




# 6. SVM Classification
svm = SVC(kernel="linear")

svm.fit(X_train, y_train)

y_pred_svm = svm.predict(X_test)

print("\nSVM Accuracy:", accuracy_score(y_test, y_pred_svm))

print("SVM Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_svm))

print("SVM Classification Report:")
print(classification_report(y_test, y_pred_svm))




# 7. Compare both models
print("\nModel Comparison")

print("KNN Accuracy:",
      accuracy_score(y_test, y_pred_knn))

print("SVM Accuracy:",
      accuracy_score(y_test, y_pred_svm))



# Check first 5 predictions
for i in range(5):
    if y_pred_knn[i] == 1:
        print("Email is Spam")
    else:
        print("Email is Not Spam")


result = pd.DataFrame({
    "Actual": y_test.values[:5],
    "Predicted": y_pred_svm[:5]
})

print(result)