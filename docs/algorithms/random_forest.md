# 🌳 Random Forest

## 🔍 Overview

**Random Forest** is an ensemble learning algorithm that builds multiple decision trees and combines their outputs to improve accuracy and reduce overfitting.

It works for both:

- Classification
- Regression

---

## 🧠 Intuition

Instead of relying on a single decision tree (which can overfit), Random Forest:

👉 Trains many trees on different subsets of data  
👉 Uses random subsets of features  
👉 Combines their predictions (majority vote / averaging)

This makes the model:

- More robust
- Less sensitive to noise
- Generally higher performing

---

## ✅ When to Use

Use Random Forest when:

- You have **tabular data**
- You want **strong baseline performance**
- You don’t want heavy feature engineering
- Interpretability is not the top priority

---

## ⚠️ When NOT to Use

Avoid when:

- You need **very fast inference**
- You require **high interpretability**
- Dataset is extremely large (can be slow)

---

## ⚙️ AlgoPipe Implementation

When you select **Random Forest** in AlgoPipe:

- Uses `sklearn.ensemble.RandomForestClassifier` or `RandomForestRegressor`
- Automatically integrates with:
  - Data preprocessing
  - Train/test split
  - Evaluation pipeline
- Applies sensible default parameters for quick start

---

## 🧩 Generated Code (Simplified)

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=None,
    random_state=42
)

model.fit(X_train, y_train)
predictions = model.predict(X_test)
```
