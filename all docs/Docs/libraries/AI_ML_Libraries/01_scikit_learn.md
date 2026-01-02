# Scikit-learn - Machine Learning Library

> **What is it?** The most popular library for traditional Machine Learning in Python
> **Install:** `pip install scikit-learn`
> **Import as:** `sklearn`

---

## Table of Contents

1. [What is Scikit-learn?](#1-what-is-scikit-learn)
2. [Installation](#2-installation)
3. [Core Concepts](#3-core-concepts)
4. [The ML Workflow](#4-the-ml-workflow)
5. [Supervised Learning - Classification](#5-supervised-learning---classification)
6. [Supervised Learning - Regression](#6-supervised-learning---regression)
7. [Unsupervised Learning - Clustering](#7-unsupervised-learning---clustering)
8. [Data Preprocessing](#8-data-preprocessing)
9. [Model Evaluation](#9-model-evaluation)
10. [Train-Test Split](#10-train-test-split)
11. [Complete Real-World Examples](#11-complete-real-world-examples)
12. [Common Mistakes](#12-common-mistakes)
13. [Quick Reference](#13-quick-reference)

---

## 1. What is Scikit-learn?

### Simple Explanation

Scikit-learn (sklearn) is like a **toolbox for teaching computers to learn patterns from data**.

```
Real-life analogy:
- You show a child 100 pictures of cats and dogs
- The child learns to recognize the difference
- Now the child can identify NEW cats and dogs they've never seen

Scikit-learn does the same thing:
- You give it data (examples)
- It learns patterns
- It makes predictions on new data
```

### What Can It Do?

| Task | What It Means | Example |
|------|---------------|---------|
| **Classification** | Predict a category | Is this email spam or not? |
| **Regression** | Predict a number | What will be the house price? |
| **Clustering** | Group similar items | Group customers by behavior |
| **Dimensionality Reduction** | Simplify data | Reduce 100 features to 10 |

### When to Use Scikit-learn vs Deep Learning?

| Use Scikit-learn When | Use TensorFlow/PyTorch When |
|-----------------------|----------------------------|
| Tabular data (spreadsheets) | Images, audio, video |
| Small to medium datasets | Huge datasets (millions) |
| Need interpretable models | Need complex patterns |
| Quick prototyping | State-of-the-art accuracy |

---

## 2. Installation

```bash
# Install scikit-learn
pip install scikit-learn

# Install with common companions
pip install scikit-learn pandas numpy matplotlib
```

### Verify Installation

```python
import sklearn
print(sklearn.__version__)
# Output: 1.3.0 (or your version)
```

---

## 3. Core Concepts

### 3.1 Features and Labels

```python
# FEATURES (X) = Input data (what you know)
# LABELS (y) = Output data (what you want to predict)

# Example: Predicting house prices
# Features (X): size, bedrooms, location
# Label (y): price

import numpy as np

# Features: [size_sqft, bedrooms, age_years]
X = np.array([
    [1500, 3, 10],
    [2000, 4, 5],
    [1200, 2, 20],
    [1800, 3, 8]
])

# Labels: prices
y = np.array([300000, 450000, 200000, 350000])

print("Features shape:", X.shape)  # Output: (4, 3) - 4 samples, 3 features
print("Labels shape:", y.shape)    # Output: (4,) - 4 labels
```

### 3.2 The Estimator API (fit, predict, transform)

Every scikit-learn model follows the same pattern:

```python
# STEP 1: Import the model
from sklearn.linear_model import LinearRegression

# STEP 2: Create the model (instantiate)
model = LinearRegression()

# STEP 3: Train the model (fit)
model.fit(X, y)  # Learn from data

# STEP 4: Make predictions (predict)
predictions = model.predict(X_new)
```

### 3.3 Visual Understanding

```
THE SCIKIT-LEARN WORKFLOW:

    Training Data                    New Data
    ┌─────────────┐                 ┌─────────────┐
    │ Features(X) │                 │ Features(X) │
    │ Labels(y)   │                 │     ???     │
    └──────┬──────┘                 └──────┬──────┘
           │                               │
           ▼                               ▼
    ┌─────────────┐                 ┌─────────────┐
    │   .fit()    │ ──────────────► │  .predict() │
    │   (Learn)   │    Model        │  (Predict)  │
    └─────────────┘                 └──────┬──────┘
                                           │
                                           ▼
                                    ┌─────────────┐
                                    │ Predictions │
                                    └─────────────┘
```

---

## 4. The ML Workflow

### Complete Pipeline

```python
# ═══════════════════════════════════════════════════════════
# STEP 1: Import libraries
# ═══════════════════════════════════════════════════════════
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ═══════════════════════════════════════════════════════════
# STEP 2: Load/Create data
# ═══════════════════════════════════════════════════════════
# Example: Predict if a student passes (1) or fails (0)
# Features: hours_studied, sleep_hours, previous_score
X = np.array([
    [2, 4, 40],   # Studied 2hrs, slept 4hrs, previous score 40
    [5, 7, 70],
    [1, 5, 30],
    [8, 8, 85],
    [3, 6, 50],
    [7, 7, 75],
    [4, 5, 55],
    [6, 8, 80],
])
y = np.array([0, 1, 0, 1, 0, 1, 0, 1])  # 0=fail, 1=pass

# ═══════════════════════════════════════════════════════════
# STEP 3: Split data (train and test)
# ═══════════════════════════════════════════════════════════
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
print(f"Training samples: {len(X_train)}")  # Output: 6
print(f"Testing samples: {len(X_test)}")    # Output: 2

# ═══════════════════════════════════════════════════════════
# STEP 4: Preprocess data (scale features)
# ═══════════════════════════════════════════════════════════
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ═══════════════════════════════════════════════════════════
# STEP 5: Train model
# ═══════════════════════════════════════════════════════════
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# ═══════════════════════════════════════════════════════════
# STEP 6: Make predictions
# ═══════════════════════════════════════════════════════════
y_pred = model.predict(X_test_scaled)
print(f"Predictions: {y_pred}")  # Output: [0 1] or similar

# ═══════════════════════════════════════════════════════════
# STEP 7: Evaluate model
# ═══════════════════════════════════════════════════════════
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")  # Output: 100.00% (on small data)
```

---

## 5. Supervised Learning - Classification

Classification = Predicting a **category** (spam/not spam, cat/dog, etc.)

### 5.1 Logistic Regression (Despite the name, it's for classification!)

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Data: Predict if customer will buy (1) or not (0)
# Features: age, salary (in thousands), time_on_site (minutes)
X = np.array([
    [25, 30, 5],
    [35, 50, 10],
    [45, 70, 15],
    [20, 25, 3],
    [30, 40, 8],
    [50, 80, 20],
    [22, 28, 4],
    [40, 60, 12],
])
y = np.array([0, 1, 1, 0, 0, 1, 0, 1])

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nDetailed Report:")
print(classification_report(y_test, y_pred))

# Predict probability (how confident is the model?)
probabilities = model.predict_proba(X_test)
print("\nProbabilities [Not Buy, Buy]:")
print(probabilities)
# Output example: [[0.7, 0.3], [0.2, 0.8]] - 30% and 80% chance to buy
```

### 5.2 Decision Tree Classifier

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

# Same data as above
X = np.array([
    [25, 30, 5], [35, 50, 10], [45, 70, 15], [20, 25, 3],
    [30, 40, 8], [50, 80, 20], [22, 28, 4], [40, 60, 12],
])
y = np.array([0, 1, 1, 0, 0, 1, 0, 1])

# Train
dt_model = DecisionTreeClassifier(max_depth=3, random_state=42)
dt_model.fit(X, y)

# Predict
new_customer = [[28, 35, 6]]
prediction = dt_model.predict(new_customer)
print(f"Will buy: {'Yes' if prediction[0] == 1 else 'No'}")

# Visualize the tree (optional)
plt.figure(figsize=(12, 8))
tree.plot_tree(dt_model, feature_names=['age', 'salary', 'time'],
               class_names=['No Buy', 'Buy'], filled=True)
plt.title("Decision Tree Visualization")
plt.savefig('decision_tree.png')
plt.show()
```

### 5.3 Random Forest Classifier (Multiple Decision Trees)

```python
from sklearn.ensemble import RandomForestClassifier

# Train
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Predict
y_pred = rf_model.predict(X_test)
print("Random Forest Accuracy:", accuracy_score(y_test, y_pred))

# Feature importance (which features matter most?)
importance = rf_model.feature_importances_
features = ['age', 'salary', 'time_on_site']
for feat, imp in zip(features, importance):
    print(f"{feat}: {imp:.3f}")
# Output example:
# age: 0.250
# salary: 0.450
# time_on_site: 0.300
```

### 5.4 K-Nearest Neighbors (KNN)

```python
from sklearn.neighbors import KNeighborsClassifier

# Train
knn_model = KNeighborsClassifier(n_neighbors=3)  # Look at 3 nearest neighbors
knn_model.fit(X_train, y_train)

# Predict
y_pred = knn_model.predict(X_test)
print("KNN Accuracy:", accuracy_score(y_test, y_pred))

# How KNN works:
# For a new point, it looks at the 3 closest training points
# and predicts the most common class among them
```

### 5.5 Support Vector Machine (SVM)

```python
from sklearn.svm import SVC

# Train
svm_model = SVC(kernel='rbf', random_state=42)
svm_model.fit(X_train, y_train)

# Predict
y_pred = svm_model.predict(X_test)
print("SVM Accuracy:", accuracy_score(y_test, y_pred))
```

---

## 6. Supervised Learning - Regression

Regression = Predicting a **continuous number** (price, temperature, etc.)

### 6.1 Linear Regression

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Data: Predict house price based on size
# Feature: size in square feet
X = np.array([[1000], [1500], [2000], [2500], [3000], [3500], [4000]])
# Label: price in dollars
y = np.array([150000, 200000, 250000, 300000, 350000, 400000, 450000])

# Train
model = LinearRegression()
model.fit(X, y)

# Model parameters
print(f"Slope (coefficient): {model.coef_[0]:.2f}")  # Price increase per sqft
print(f"Intercept: {model.intercept_:.2f}")          # Base price
# Output: Slope: 100.00, Intercept: 50000.00
# Meaning: Price = 100 * size + 50000

# Predict
new_house = [[2200]]
predicted_price = model.predict(new_house)
print(f"Predicted price for 2200 sqft: ${predicted_price[0]:,.2f}")
# Output: Predicted price for 2200 sqft: $270,000.00

# Evaluate
y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.4f}")  # 1.0 = perfect, 0 = bad
```

### 6.2 Polynomial Regression (For Curved Relationships)

```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np

# Data with curved relationship
X = np.array([[1], [2], [3], [4], [5], [6], [7]])
y = np.array([1, 4, 9, 16, 25, 36, 49])  # y = x²

# Create polynomial features (x, x², x³, etc.)
poly = PolynomialFeatures(degree=2)  # Include up to x²
X_poly = poly.fit_transform(X)
print("Original X:", X.flatten())
print("Polynomial X:\n", X_poly)
# Output: [[1, 1, 1], [1, 2, 4], [1, 3, 9], ...] = [1, x, x²]

# Train
model = LinearRegression()
model.fit(X_poly, y)

# Predict
X_new = np.array([[8]])
X_new_poly = poly.transform(X_new)
prediction = model.predict(X_new_poly)
print(f"Predicted value for x=8: {prediction[0]:.2f}")  # Output: 64.00
```

### 6.3 Ridge and Lasso Regression (With Regularization)

```python
from sklearn.linear_model import Ridge, Lasso

# Ridge: Prevents overfitting by penalizing large coefficients
ridge = Ridge(alpha=1.0)  # alpha = regularization strength
ridge.fit(X_train, y_train)
ridge_pred = ridge.predict(X_test)

# Lasso: Same as Ridge but can eliminate features (set coefficients to 0)
lasso = Lasso(alpha=1.0)
lasso.fit(X_train, y_train)
lasso_pred = lasso.predict(X_test)

print("Ridge coefficients:", ridge.coef_)
print("Lasso coefficients:", lasso.coef_)  # Some might be 0
```

---

## 7. Unsupervised Learning - Clustering

Clustering = Grouping similar items WITHOUT labels

### 7.1 K-Means Clustering

```python
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# Data: Customer spending patterns
# Features: annual_income, spending_score
X = np.array([
    [15, 39], [16, 81], [17, 6], [18, 77], [19, 40],
    [70, 40], [71, 70], [72, 30], [73, 75], [74, 50],
    [40, 50], [41, 55], [42, 45], [43, 60], [44, 52],
])

# Create and train K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Get cluster labels for each point
labels = kmeans.labels_
print("Cluster labels:", labels)
# Output: [0 0 0 0 0 1 1 1 1 1 2 2 2 2 2] (or similar)

# Get cluster centers
centers = kmeans.cluster_centers_
print("Cluster centers:\n", centers)

# Predict cluster for new data
new_customer = [[25, 50]]
cluster = kmeans.predict(new_customer)
print(f"New customer belongs to cluster: {cluster[0]}")

# Visualize
plt.figure(figsize=(10, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=100)
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200, label='Centers')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.title('Customer Segments')
plt.legend()
plt.savefig('kmeans_clusters.png')
plt.show()
```

### 7.2 Finding Optimal Number of Clusters (Elbow Method)

```python
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Try different numbers of clusters
inertias = []
K_range = range(1, 10)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)  # Sum of squared distances

# Plot elbow curve
plt.figure(figsize=(8, 5))
plt.plot(K_range, inertias, 'bo-')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia')
plt.title('Elbow Method - Find Optimal K')
plt.savefig('elbow_method.png')
plt.show()

# Look for the "elbow" - where the curve bends
```

### 7.3 DBSCAN (Density-Based Clustering)

```python
from sklearn.cluster import DBSCAN

# DBSCAN doesn't need you to specify number of clusters
dbscan = DBSCAN(eps=10, min_samples=2)
labels = dbscan.fit_predict(X)

print("DBSCAN labels:", labels)
# -1 means noise (doesn't belong to any cluster)

n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
print(f"Number of clusters found: {n_clusters}")
```

---

## 8. Data Preprocessing

### 8.1 Handling Missing Values

```python
from sklearn.impute import SimpleImputer
import numpy as np

# Data with missing values (NaN)
X = np.array([
    [1, 2, np.nan],
    [3, np.nan, 6],
    [7, 8, 9],
    [np.nan, 11, 12]
])

# Strategy: 'mean', 'median', 'most_frequent', 'constant'
imputer = SimpleImputer(strategy='mean')
X_filled = imputer.fit_transform(X)

print("Original:\n", X)
print("\nFilled:\n", X_filled)
# NaN replaced with column mean
```

### 8.2 Feature Scaling

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

X = np.array([
    [100, 0.001],
    [200, 0.002],
    [300, 0.003],
])

# StandardScaler: Mean=0, Std=1 (most common)
scaler = StandardScaler()
X_standard = scaler.fit_transform(X)
print("StandardScaler:\n", X_standard)

# MinMaxScaler: Range [0, 1]
minmax = MinMaxScaler()
X_minmax = minmax.fit_transform(X)
print("\nMinMaxScaler:\n", X_minmax)
```

### 8.3 Encoding Categorical Variables

```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np

# Label Encoding: Convert categories to numbers
categories = np.array(['red', 'blue', 'green', 'red', 'blue'])
le = LabelEncoder()
encoded = le.fit_transform(categories)
print("Label Encoded:", encoded)  # Output: [2 0 1 2 0]
print("Classes:", le.classes_)    # Output: ['blue' 'green' 'red']

# One-Hot Encoding: Convert to binary columns
ohe = OneHotEncoder(sparse_output=False)
X_categorical = np.array([['red'], ['blue'], ['green'], ['red']])
X_onehot = ohe.fit_transform(X_categorical)
print("\nOne-Hot Encoded:\n", X_onehot)
# Output:
# [[0. 0. 1.]   # red
#  [1. 0. 0.]   # blue
#  [0. 1. 0.]   # green
#  [0. 0. 1.]]  # red
```

---

## 9. Model Evaluation

### 9.1 Classification Metrics

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report
)

# True labels and predictions
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
y_pred = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]

# Accuracy: Overall correctness
accuracy = accuracy_score(y_true, y_pred)
print(f"Accuracy: {accuracy:.2f}")  # Output: 0.80

# Precision: Of predicted positives, how many are correct?
precision = precision_score(y_true, y_pred)
print(f"Precision: {precision:.2f}")  # Output: 0.80

# Recall: Of actual positives, how many did we find?
recall = recall_score(y_true, y_pred)
print(f"Recall: {recall:.2f}")  # Output: 0.80

# F1 Score: Balance of precision and recall
f1 = f1_score(y_true, y_pred)
print(f"F1 Score: {f1:.2f}")  # Output: 0.80

# Confusion Matrix
cm = confusion_matrix(y_true, y_pred)
print("\nConfusion Matrix:")
print(cm)
# Output:
# [[3 1]    <- [True Negative, False Positive]
#  [1 5]]   <- [False Negative, True Positive]

# Full Report
print("\nClassification Report:")
print(classification_report(y_true, y_pred))
```

### 9.2 Regression Metrics

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

y_true = [100, 200, 300, 400, 500]
y_pred = [110, 190, 310, 380, 520]

# Mean Squared Error (MSE)
mse = mean_squared_error(y_true, y_pred)
print(f"MSE: {mse:.2f}")  # Output: 260.00

# Root Mean Squared Error (RMSE)
rmse = np.sqrt(mse)
print(f"RMSE: {rmse:.2f}")  # Output: 16.12

# Mean Absolute Error (MAE)
mae = mean_absolute_error(y_true, y_pred)
print(f"MAE: {mae:.2f}")  # Output: 14.00

# R² Score (1 = perfect, 0 = bad)
r2 = r2_score(y_true, y_pred)
print(f"R² Score: {r2:.4f}")  # Output: 0.9870
```

---

## 10. Train-Test Split

### 10.1 Basic Split

```python
from sklearn.model_selection import train_test_split

X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Split: 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # 20% for testing
    random_state=42     # For reproducibility
)

print(f"Training size: {len(X_train)}")  # Output: 8
print(f"Testing size: {len(X_test)}")    # Output: 2
```

### 10.2 Cross-Validation

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

# 5-Fold Cross Validation
model = LogisticRegression()
scores = cross_val_score(model, X, y, cv=5)  # 5 folds

print("Scores for each fold:", scores)
print(f"Mean accuracy: {scores.mean():.4f}")
print(f"Std deviation: {scores.std():.4f}")
```

---

## 11. Complete Real-World Examples

### Example 1: Predicting Diabetes

```python
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Load dataset
diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target

print("Feature names:", diabetes.feature_names)
print("Data shape:", X.shape)  # (442, 10) - 442 samples, 10 features

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train
model = Ridge(alpha=1.0)
model.fit(X_train_scaled, y_train)

# Predict
y_pred = model.predict(X_test_scaled)

# Evaluate
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"\nResults:")
print(f"RMSE: {rmse:.2f}")
print(f"R² Score: {r2:.4f}")
```

### Example 2: Iris Flower Classification

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load famous Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

print("Feature names:", iris.feature_names)
print("Target names:", iris.target_names)  # setosa, versicolor, virginica

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2%}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Predict new flower
new_flower = [[5.1, 3.5, 1.4, 0.2]]  # sepal length, sepal width, petal length, petal width
prediction = model.predict(new_flower)
print(f"\nNew flower prediction: {iris.target_names[prediction[0]]}")
```

### Example 3: Customer Segmentation

```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

# Customer data: [annual_income, spending_score]
customers = np.array([
    [15, 39], [15, 81], [16, 6], [16, 77], [17, 40],
    [18, 76], [18, 6], [19, 94], [19, 3], [20, 72],
    [70, 29], [71, 41], [72, 35], [73, 14], [74, 66],
    [75, 55], [76, 52], [77, 60], [78, 48], [79, 59],
    [40, 42], [41, 52], [42, 47], [43, 58], [44, 43],
])

# Scale the data
scaler = StandardScaler()
customers_scaled = scaler.fit_transform(customers)

# Find optimal clusters
inertias = []
for k in range(1, 8):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(customers_scaled)
    inertias.append(kmeans.inertia_)

# Apply K-Means with optimal k (let's say 3)
kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(customers_scaled)

# Analyze segments
for i in range(3):
    segment = customers[labels == i]
    print(f"\nSegment {i}:")
    print(f"  Average Income: ${segment[:, 0].mean():.0f}k")
    print(f"  Average Spending: {segment[:, 1].mean():.0f}")
    print(f"  Count: {len(segment)} customers")

# Visualize
plt.figure(figsize=(10, 6))
scatter = plt.scatter(customers[:, 0], customers[:, 1], c=labels, cmap='viridis', s=100)
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score')
plt.title('Customer Segments')
plt.colorbar(scatter, label='Segment')
plt.savefig('customer_segments.png')
plt.show()
```

---

## 12. Common Mistakes

### Mistake 1: Not Scaling Data

```python
# WRONG - Features have different scales
X = np.array([[1000, 0.001], [2000, 0.002]])  # income vs tiny decimal
model.fit(X, y)  # Model might ignore tiny features!

# CORRECT - Scale first
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
model.fit(X_scaled, y)
```

### Mistake 2: Data Leakage (Fitting Scaler on Test Data)

```python
# WRONG - Scaler sees test data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Fits on ALL data including test
X_train, X_test = train_test_split(X_scaled)

# CORRECT - Fit only on training data
X_train, X_test, y_train, y_test = train_test_split(X, y)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # Fit on train only
X_test_scaled = scaler.transform(X_test)         # Just transform test
```

### Mistake 3: Using Accuracy for Imbalanced Data

```python
# If 95% of data is class 0, predicting always 0 gives 95% accuracy!
# Use F1 score, precision, recall instead

from sklearn.metrics import f1_score, classification_report
print(classification_report(y_test, y_pred))
```

---

## 13. Quick Reference

### Algorithms Cheat Sheet

| Task | Algorithm | When to Use |
|------|-----------|-------------|
| Classification | LogisticRegression | Binary classification, interpretable |
| Classification | RandomForestClassifier | General purpose, handles non-linear |
| Classification | SVC | Small-medium data, good accuracy |
| Classification | KNeighborsClassifier | Simple, no training needed |
| Regression | LinearRegression | Simple linear relationships |
| Regression | Ridge/Lasso | When you have many features |
| Regression | RandomForestRegressor | Non-linear relationships |
| Clustering | KMeans | Known number of clusters |
| Clustering | DBSCAN | Unknown clusters, handles noise |

### Common Imports

```python
# Data handling
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder

# Classification
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# Regression
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor

# Clustering
from sklearn.cluster import KMeans, DBSCAN

# Metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import confusion_matrix, classification_report

# Datasets
from sklearn.datasets import load_iris, load_diabetes, load_digits
```

### Workflow Template

```python
# 1. Import
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.MODEL import MODEL_NAME
from sklearn.metrics import METRIC

# 2. Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 3. Scale (if needed)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. Train
model = MODEL_NAME()
model.fit(X_train, y_train)

# 5. Predict
y_pred = model.predict(X_test)

# 6. Evaluate
score = METRIC(y_test, y_pred)
print(f"Score: {score}")
```

---

## Summary

Scikit-learn is the foundation of Machine Learning in Python. Master these concepts:

1. **fit()** - Train the model
2. **predict()** - Make predictions
3. **transform()** - Preprocess data
4. **train_test_split()** - Split your data
5. **StandardScaler()** - Scale your features
6. **Classification** - Predict categories
7. **Regression** - Predict numbers
8. **Clustering** - Group similar items

Start with simple models (LogisticRegression, LinearRegression) before moving to complex ones!
