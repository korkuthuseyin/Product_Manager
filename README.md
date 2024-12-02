# Product Manager

A simple Product Management application built using Python's Tkinter library and PostgreSQL for database management. This application allows you to manage products, including adding, updating, deleting, and listing products. It connects to a PostgreSQL database to store product information.

## Features

- **Add Product**: Insert new products into the database.
- **Update Product**: Modify existing product details like barcode, name, stock, purchase price, or sell price.
- **Delete Product**: Remove a product from the database by its ID.
- **List Products**: View all products stored in the database in a formatted table.

## Technologies

- **Python 3.11.6**
- **Tkinter**: GUI framework for Python.
- **psycopg2**: PostgreSQL database adapter for Python.
- **PostgreSQL**: Relational database to store product data.

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/korkuthuseyin/Product_Manager.git
  
2. Set up PostgreSQL database:
**Create a PostgreSQL database named yzv104_term_project.**
  - Create a table called products with the following schema:
   ```sql
   CREATE TABLE products (
       product_id SERIAL PRIMARY KEY,
       barcode VARCHAR(50) NOT NULL,
       name VARCHAR(100) NOT NULL,
       stock INTEGER NOT NULL,
       purchase_price DECIMAL(10, 2) NOT NULL,
       sell_price DECIMAL(10, 2) NOT NULL
   );
   ```
3. Configure the database connection in main.py
   ```python
    DB_HOST = 'localhost'
    DB_NAME = 'yzv104_term_project'
    DB_USER = 'postgres'
    DB_PASS = 'postgres'
   ```

4. Run the application:
   ```bash
     python3 main.py
   ```


