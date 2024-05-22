import tkinter as tk
import psycopg2
from tkinter import messagebox


# Database connection parameters
DB_HOST = 'localhost'
DB_NAME = 'yzv104_term_project'
DB_USER = 'postgres'
DB_PASS = 'postgres'

# Database connection
def connect_db():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )


# Add product
def add_product():
    barcode = entry_barcode.get()
    name = entry_name.get()
    stock = entry_stock.get()
    purchase_price = entry_purchase_price.get()
    sell_price = entry_sell_price.get()

    if barcode and name and stock and purchase_price and sell_price:
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO products (barcode, name, stock, purchase_price, sell_price) VALUES (%s, %s, %s, %s, %s)", 
                           (barcode, name, stock, purchase_price, sell_price))
            conn.commit()
            cursor.close()
            conn.close()
            list_products()
            clear_entries()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input Error", "Please fill all fields")

# Delete product
def delete_product():
    product_id = entry_id.get()
    
    if product_id:
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM products WHERE product_id = %s", (product_id,))
            conn.commit()
            cursor.close()
            conn.close()
            list_products()
            clear_entries()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input Error", "Please fill the product ID")

# Update product
def update_product():
    product_id = entry_id.get()
    barcode = entry_barcode.get()
    name = entry_name.get()
    stock = entry_stock.get()
    purchase_price = entry_purchase_price.get()
    sell_price = entry_sell_price.get()

    if product_id and (barcode or name or stock or purchase_price or sell_price):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            if barcode:
                cursor.execute("UPDATE products SET barcode = %s WHERE product_id = %s", (barcode, product_id))
            if name:
                cursor.execute("UPDATE products SET name = %s WHERE product_id = %s", (name, product_id))
            if stock:
                cursor.execute("UPDATE products SET stock = %s WHERE product_id = %s", (stock, product_id))
            if purchase_price:
                cursor.execute("UPDATE products SET purchase_price = %s WHERE product_id = %s", (purchase_price, product_id))
            if sell_price:
                cursor.execute("UPDATE products SET sell_price = %s WHERE product_id = %s", (sell_price, product_id))
            conn.commit()
            cursor.close()
            conn.close()
            list_products()
            clear_entries()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input Error", "Please fill the product ID and at least one field to update")


# Clear entry fields
def clear_entries():
    entry_id.delete(0, tk.END)
    entry_barcode.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_stock.delete(0, tk.END)
    entry_purchase_price.delete(0, tk.END)
    entry_sell_price.delete(0, tk.END)

# Function to format product data into columns
def format_product(product):
    return f"{product[0]:<5} {product[1]:<15} {product[2]:<30} {product[3]:<10} {product[4]:<15} {product[5]:<15}"

# Function to list products in the table view
def list_products():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        listbox.delete(0, tk.END)

        # Insert column titles as the first row
        listbox.insert(tk.END, format_product(('ID', 'Barcode', 'Name', 'Stock', 'Purchase Price', 'Sell Price')))

        for product in products:
            formatted_product = format_product(product)
            listbox.insert(tk.END, formatted_product)
        cursor.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Tkinter setup
root = tk.Tk()
root.title("Product Management")

# Labels
tk.Label(root, text="Product ID").grid(row=0, column=0, padx=5, pady=5)
tk.Label(root, text="Barcode").grid(row=1, column=0, padx=5, pady=5)
tk.Label(root, text="Name").grid(row=2, column=0, padx=5, pady=5)
tk.Label(root, text="Stock").grid(row=3, column=0, padx=5, pady=5)
tk.Label(root, text="Purchase Price").grid(row=4, column=0, padx=5, pady=5)
tk.Label(root, text="Sell Price").grid(row=5, column=0, padx=5, pady=5)

# Entries
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1, padx=5, pady=5)

entry_barcode = tk.Entry(root)
entry_barcode.grid(row=1, column=1, padx=5, pady=5)

entry_name = tk.Entry(root)
entry_name.grid(row=2, column=1, padx=5, pady=5)

entry_stock = tk.Entry(root)
entry_stock.grid(row=3, column=1, padx=5, pady=5)

entry_purchase_price = tk.Entry(root)
entry_purchase_price.grid(row=4, column=1, padx=5, pady=5)

entry_sell_price = tk.Entry(root)
entry_sell_price.grid(row=5, column=1, padx=5, pady=5)

# Buttons
btn_add = tk.Button(root, text="Add Product", command=add_product)
btn_add.grid(row=6, column=0, padx=5, pady=5)

btn_delete = tk.Button(root, text="Delete Product", command=delete_product)
btn_delete.grid(row=6, column=1, padx=5, pady=5)

btn_update = tk.Button(root, text="Update Product", command=update_product)
btn_update.grid(row=6, column=2, padx=5, pady=5)

btn_list = tk.Button(root, text="List Products", command=list_products)
btn_list.grid(row=6, column=3, padx=5, pady=5)

# Listbox to display products in table view
listbox = tk.Listbox(root, width=120, font=('Courier', 10))
listbox.grid(row=7, column=0, columnspan=4, padx=5, pady=5)



# Initialize list
list_products()
# Run the Tkinter event loop
root.mainloop()
