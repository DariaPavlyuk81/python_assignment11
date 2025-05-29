#Task2
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('../db/lesson.db')

query = """
SELECT o.order_id, 
       SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
"""
df = pd.read_sql_query(query, conn)

#cumulative revenue
df['cumulative'] = df['total_price'].cumsum()

#plot cumulative revenue

plt.figure(figsize=(12, 6))
plt.plot(df['order_id'], df['cumulative'], marker='o', color='blue')

plt.title('Cumulative Revenue vs Order ID')
plt.xlabel('Order ID')
plt.ylabel('Cumulative Revenue ($)')
plt.grid(True)
plt.tight_layout()

plt.show()