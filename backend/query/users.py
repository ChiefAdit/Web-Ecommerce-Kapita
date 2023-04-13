import connectdb
import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def check_passsword(password, hashed_password):
    return bcrypt.checkpw(pasword.encode('utf-8'), hashed_password.encode('utf-8'))

def query_login_admin(email, password):
    conn = connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT email, password, name, role FROM _672020277_ecommerce_users WHERE email = %s AND role = 'admin'", (email,))
        admin = cur.fetchone()
        cur.close()
        if admin is not None and check_password(password, admin[1]):
            return admin
        else:
            return None
    else:
        return None

def query_login_customer(email, password):
    conn = connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT email, password, name, role FROM _672020277_ecommerce_users WHERE email = %s AND role = 'customer'", (email,))
        customer = cur.fetchone()
        cur.close()
        if customer is not None and check_password(password, customer[1]):
            return customer
        else:
            return None
    else:
        return None

def query_register(email, password, name):
    conn=connectdb.test_connection()
    if conn is not None:
        hashed_password = hash_password(password)
        cur = conn.cursor()
        cur.execute("INSERT INTO _672020277_ecommerce_users (email, password, name, role) VALUES (%s, %s, %s, 'customer')", (email, hashed_password, name))
        conn.commit()
        cur.close()
        return True
    else:
        print("Connection Failed")
        return False

def query_register_admin(email, password, name):
    conn=connectdb.test_connection()
    if conn is not None:
        hashed_password = hash_password(password)
        cur = conn.cursor()
        cur.execute("INSERT INTO _672020277_ecommerce_users (email, password, name, role) VALUES (%s, %s, %s, 'admin')", (email, hashed_password, name))
        conn.commit()
        cur.close()
        return True
    else:
        print("Connection Failed")
        return False

def query_get_all_users():
    conn=connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT email, name FROM _672020277_ecommerce_users WHERE role = 'customer'")
        rows = cur.fetchall()
        cur.close()
        return rows
    else:
        return None

def query_get_user_by_email(email):
    conn=connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT email, password, name, role FROM _672020277_ecommerce_users WHERE email = %s AND role = 'customer'", (email,))
        row = cur.fetchone()
        cur.close()
        if row is not None:
            row = (row[0], "", row[2], row[3])
        return row
    else:
        return None

def query_update_user_by_email(email, password, name):
    conn=connectdb.test_connection()
    if conn is not None:
        hashed_password = hash_password(password)
        cur = conn.cursor()
        cur.execute("UPDATE _672020277_ecommerce_users SET email = %s, password = %s, name = %s WHERE email = %s AND role = 'customer'", (email, hashed_password, name, email))
        conn.commit()
        cur.close()
        return True
    else:
        return False

def query_delete_user_by_email(email):
    conn=connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("DELETE FROM _672020277_ecommerce_users WHERE email = %s AND role = 'customer'", (email,))
        conn.commit()
        cur.close()
        return True
    else:
        return False

#hitung jumlah data Customer
def query_count_users():
    conn=connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM _672020277_ecommerce_users WHERE role = 'customer'")
        count = cur.fetchone()
        cur.close()
        return count[0]
    else:
        return None
#hitung jumlah data Admin
def query_count_admin():
    conn=connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM _672020277_ecommerce_users WHERE role = 'admin'")
        count = cur.fetchone()
        cur.close()
        return count[0]
    else:
        return None

#hitung semua data user 
def query_count_all_users():
    conn=connectdb.test_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM _672020277_ecommerce_users")
        count = cur.fetchone()
        cur.close()
        return count[0]
    else:
        return None