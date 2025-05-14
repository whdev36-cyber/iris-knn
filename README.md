# 🌸 iris-knn

This project uses the **K-Nearest Neighbors (KNN)** algorithm to classify **Iris flowers** based on their physical characteristics. It is built with `scikit-learn` and is a great starting point for beginners in machine learning.

GitHub Repository: [https://github.com/whdev36-cyber/iris-knn](https://github.com/whdev36-cyber/iris-knn)

---

## 📊 Dataset

- **Source:** [Iris Dataset - UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris)
- **Samples:** 150 flower records with 4 features:
  - Sepal length (cm)
  - Sepal width (cm)
  - Petal length (cm)
  - Petal width (cm)
- **Classes:**
  - Setosa
  - Versicolor
  - Virginica

---

## ⚙️ Features

- Data loading using `scikit-learn`
- Model training using KNN
- Train/test split
- Performance evaluation (accuracy, classification report, confusion matrix)
- Simple visualization using `matplotlib`

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/whdev36-cyber/iris-knn.git
cd iris-knn
````

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the classifier

```bash
python iris_knn_classifier.py
```

If you're running in a non-GUI environment, the plot will be saved as `iris_knn_plot.png`.

---

## 📈 Output

* Model accuracy printed in the terminal
* Classification report and confusion matrix
* A scatter plot of petal length vs. petal width, saved as an image

---

## 📦 Requirements

* `scikit-learn`
* `matplotlib`
* `pandas`

(Install with `pip install -r requirements.txt`)

---

## 🧠 Author

* GitHub: [@whdev36-cyber](https://github.com/whdev36-cyber)

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

