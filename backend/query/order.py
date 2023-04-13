import connectdb 


def query_create_order(customer_email, product_id, quantity, price):
    conn = connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()
        
        # Simpan informasi order ke database
        cur.execute("INSERT INTO _672020277_ecommerce_order_item (customer_email, product_id, quantity, price) VALUES (%s, %s, %s, %s)", (customer_email, product_id, quantity, price))
        conn.commit()
        cur.close()
        return True
    else:
        print("Connection Failed")
        return False
        


        