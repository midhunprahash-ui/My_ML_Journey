# 🛠️ Feature Engineering with Pandas

Feature engineering is the process of creating new input features from existing data to improve model performance. This can include transformations, extractions, encodings, and combining multiple columns.

---

## 🔁 1. Creating New Features

```python
# Total amount from quantity and price
df['total_amount'] = df['quantity'] * df['price']

# Combine two columns
df['full_name'] = df['first_name'] + ' ' + df['last_name']