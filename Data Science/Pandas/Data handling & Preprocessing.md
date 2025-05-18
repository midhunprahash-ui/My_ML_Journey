# 📊 Data Handling & Preprocessing with Pandas

Before training a model, your data needs to be cleaned, formatted, and transformed into a machine-learning-friendly shape. This step is called **data preprocessing**, and it includes selecting relevant features, transforming values, encoding categories, and more.

---

## 🧽 1. Cleaning Column Names

```python
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')