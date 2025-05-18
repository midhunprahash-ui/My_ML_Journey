# 🧹 Data Cleaning with Pandas

Cleaning your dataset is a vital step before any analysis or machine learning model training. Poor quality data = poor quality insights. Here's a structured guide using **Pandas** for effective data cleaning.

---

## 🔍 1. Check for Missing Values

```python
df.isnull().sum()       # Total missing values per column
df.isnull().mean()      # Proportion of missing values
df[df.isnull().any(axis=1)]   # Rows with at least one missing value