import connectdb
import os
from werkzeug.utils import secure_filename



#buat query untuk menampilankan semua data produk
def query_get_all_products():
    conn = connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT name, description, CAST(price AS float) AS price, stock, product_id FROM \"_672020277_ecommerce_products\"")
        rows = cur.fetchall()
        cur.close()
        products = []
        for row in rows:
            product = {
                "name": row[0],
                "description": row[1],
                "price": row[2],
                "stock": row[3],
                "product_id": row[4]
                
            }
            products.append(product)
        return products
    else:
        return None
  



def query_add_product(name, description, price, stock):
    conn = connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()
        
        # Simpan gambar ke folder di backend
      
        
        # Simpan informasi produk ke database
        cur.execute("INSERT INTO _672020277_ecommerce_products (name, description, price, stock) VALUES (%s, %s, %s, %s)", (name, description, price, stock))
        conn.commit()
        cur.close()
        return True
    else:
        print("Connection Failed")
        return False


#delete produk
def query_delete_product(product_id):
    conn=connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("DELETE FROM _672020277_ecommerce_products WHERE product_id = %s", (product_id,))
        conn.commit()
        cur.close()
        return True
    else:
        print("Connection Failed")
        return False

#update produk
def query_update_product(name, description, price, stock, product_id):
    conn=connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("UPDATE _672020277_ecommerce_products SET name = %s, description = %s, price = %s, stock = %s WHERE product_id = %s", (name, description, price, stock,  product_id))
        conn.commit()
        cur.close()
        return True
    else:
        print("Connection Failed")
        return False

#ambil data produk berdasarkan id
def query_get_product_by_id(product_id):
    conn=connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()
        
        cur.execute("SELECT name, description, CAST(price AS float) AS price, stock, product_id FROM public.\"_672020277_ecommerce_products\" WHERE product_id = %s", (product_id,))
        rows = cur.fetchall()
        cur.close()
        products = []
        for row in rows:
            product = {
                "name": row[0],
                "description": row[1],
                "price": row[2],
                "stock": row[3],
                "product_id": row[4]
                
            }
            products.append(product)
        return products
    else:
        return None

#hitung jumlah data produk
def query_count_product():
    conn=connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM public.\"_672020277_ecommerce_products\"")
        count = cur.fetchall()
        cur.close()
        return count[0]
    else:
        return None