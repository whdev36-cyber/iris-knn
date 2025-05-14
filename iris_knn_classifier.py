from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt

# STEP 1: LOAD DATASET
iris = load_iris()
X = iris.data
y = iris.target


# STEP 2: DATA TRAIN AND TEST
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# STEP 3: CREATE KNN MODEL
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)


# STEP 4: PREDICT
y_pred = knn.predict(X_test)


# STEP 5: EVALUATION OF THE RESULT
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))


# STEP 6: VISUALIZATION (PETAL LENGTH VS PETAL WIDTH)
df = pd.DataFrame(X, columns=iris.feature_names)
df['target'] = y
plt.figure(figsize=(8, 6))
for i, target_name in enumerate(iris.target_names):
    plt.scatter(df[df['target'] == i]['petal length (cm)'],
                df[df['target'] == i]['petal width (cm)'],
                label=target_name)

plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Iris Flower Classification (KNN)')
plt.legend()
plt.grid(True)
# plt.show()

plt.savefig("iris_knn_plot.png")
print("ris_knn_plot.png")
