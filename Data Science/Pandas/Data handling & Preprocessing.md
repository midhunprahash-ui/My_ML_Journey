# 📊 Data Handling & Preprocessing with Pandas

Before training a model, your data needs to be cleaned, formatted, and transformed into a machine-learning-friendly shape. This step is called **data preprocessing**, and it includes selecting relevant features, transforming values, encoding categories, and more.

---

## 🧽 1. Cleaning Column Names

```python
# Check missing values
print(df.isnull().sum())

# Fill missing values
df['column'].fillna(df['column'].mean(), inplace=True)  # with mean
df['column'].fillna(df['column'].mode()[0], inplace=True)  # with mode
df['column'].fillna(df['column'].median(), inplace=True)  # with median
df['column'].fillna(method='ffill', inplace=True)  # forward fill
df['column'].fillna(method='bfill', inplace=True)  # backward fill

# Drop rows with missing values
df.dropna(subset=['column'], inplace=True)

# Check duplicates
print(df.duplicated().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)
df.drop_duplicates(subset=['column'], inplace=True)  # based on specific columns
