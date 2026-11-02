import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


# Load dataset with a different encoding
df = pd.read_csv('sales_data_sample.csv', encoding ="unicode_escape")
df

df = df.dropna()

# Select numerical columns for clustering
# Assume we are clustering based on 'SALES', 'QUANTITYORDERED', 'PRICEEACH'
X = df[[ 'QUANTITYORDERED', 'PRICEEACH','SALES']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)



# 5. Elbow method
inertia = []
K = range(1, 11)

for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)


# 6. Plot elbow graph
plt.figure(figsize=(8, 6))
plt.plot(K, inertia, "bo-")

plt.xlabel("Number of clusters (k)")
plt.ylabel("Inertia")
plt.title("Elbow Method for Optimal K")

plt.show()



# 7. Apply K-Means
optimal_k = 4

kmeans = KMeans(n_clusters=optimal_k, random_state=42)
df["Cluster"] = kmeans.fit_predict(X_scaled)

# 8. Display cluster assignments
df[['SALES', 'QUANTITYORDERED', 'PRICEEACH', 'Cluster']]



# 9. Visualize clusters
plt.scatter(df["QUANTITYORDERED"],
            df["SALES"],
            c=df["Cluster"])

plt.xlabel("Quantity Ordered")
plt.ylabel("Sales")
plt.title("Sales Clustering")
plt.show()