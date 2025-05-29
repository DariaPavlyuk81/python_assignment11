#Task1
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

try:
    conn = sqlite3.connect('../db/lesson.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    if tables:
        print("Successfully connected to the database. Tables found:")
        for table in tables:
            print(table[0])
    else:
        print("Connected but no tables found.")
        
    
    
    query = """
    SELECT last_name, 
       SUM(price * quantity) AS revenue
    FROM employees e
    JOIN orders o ON e.employee_id = o.employee_id
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON l.product_id = p.product_id
    GROUP BY e.employee_id;
    """


    employee_results = pd.read_sql_query(query, conn)
    conn.close()

    employee_results = employee_results.sort_values(by='revenue', ascending=False)

    plt.figure(figsize=(12, 6))
    plt.bar(employee_results['last_name'], employee_results['revenue'], color='teal')

    plt.title('Employee Revenue from Sales')
    plt.xlabel('Employee Last Name')
    plt.ylabel('Revenue ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()

except Exception as e:
    print("Error:", e)
