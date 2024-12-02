import sqlite3
import pandas as pd
def create_database():
    conn = sqlite3.connect('database.db')
    cursor=conn.cursor()

    # Load CSV datasets
    customers = pd.read_csv('https://raw.githubusercontent.com/SobiaNoorAI/Python/main/Ecommerce%20Sales%20Analysis/data/Customers_Large.csv')
    orders = pd.read_csv('https://raw.githubusercontent.com/SobiaNoorAI/Python/main/Ecommerce%20Sales%20Analysis/data/Orders_Large.csv')
    products = pd.read_csv('https://raw.githubusercontent.com/SobiaNoorAI/Python/main/Ecommerce%20Sales%20Analysis/data/Products_Large.csv')
    sales = pd.read_csv('https://raw.githubusercontent.com/SobiaNoorAI/Python/main/Ecommerce%20Sales%20Analysis/data/Sales_Large.csv')

    # Write data into database tables
    orders.to_sql('orders_large', conn, if_exists='replace', index=False)
    products.to_sql('products_large', conn, if_exists='replace', index=False)
    customers.to_sql('customers_large', conn, if_exists='replace', index=False)
    sales.to_sql('sales_large', conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()
    print("Database created and populated successfully.")

if __name__ == "__main__":
    create_database()