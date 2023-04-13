import jwt
from datetime import datetime, timedelta
from flask import Flask, request, redirect, url_for, session, render_template, flash
import requests
from flask_caching import Cache


app = Flask(__name__)
app.secret_key = 'secretkey'
#auto reload
app.config['TEMPLATES_AUTO_RELOAD'] = True
cache = Cache(app, config={'CACHE_TYPE': 'simple'})



#section untuk customer




def get_customer_email():
    if 'email' in session:
        return session['email']
    return None

# untuk customer
"""
@app.route("/", methods=['GET'])
def index():
    if "email" in session and "token" in session:
        # Ambil email dan token dari session
        emailCustomer = get_customer_email()
        tokenCustomer = session["token"]
         # Request ke API produk
        # Tampilkan halaman index.html
        
        # Set header Authorization dengan token JWT
        headers = {"Authorization": f"Bearer {tokenCustomer}"}
        data = {}
        try:
            response = requests.get('https://backend-adit-5zn7xh2gqq-et.a.run.app/product')
            if response.status_code == 200:
                data = response.json()
                print(data)
            else:
                print("ERROR | Get products data |", response.status_code)
        except Exception as e:
            print("ERROR | Get products data |", e) 


        # Tampilkan halaman index.html
        return render_template("index.html", user=emailCustomer, products=data["products"])
    else:
        return redirect(url_for('loginCustomer'))

"""

#index customer tanpa token

@app.route("/", methods=['GET'])
@cache.cached(timeout=3)
def index():
    if "email" in session and "token" in session:
        # Ambil email dan token dari session
        emailCustomer = get_customer_email()
        tokenCustomer = session["token"]
         # Request ke API produk
        # Tampilkan halaman index.html
        
        # Set header Authorization dengan token JWT
        headers = {"Authorization": f"Bearer {tokenCustomer}"}
        data = {}
        try:
            response = requests.get('https://backend-adit-5zn7xh2gqq-et.a.run.app/product')
            if response.status_code == 200:
                data = response.json()
                print(data)
            else:
                print("ERROR | Get products data |", response.status_code)
        except Exception as e:
            print("ERROR | Get products data |", e) 


        # Tampilkan halaman index.html
        return render_template("index.html", user=emailCustomer, products=data["products"])
    else:
        # Request ke API produk
        # Tampilkan halaman index.html
        
        data = {}
        try:
            response = requests.get('https://backend-adit-5zn7xh2gqq-et.a.run.app/product')
            if response.status_code == 200:
                data = response.json()
                print(data)
            else:
                print("ERROR | Get products data |", response.status_code)
        except Exception as e:
            print("ERROR | Get products data |", e) 


        # Tampilkan halaman index.html
        return render_template("index.html", products=data["products"])

@app.route("/loginCustomer", methods=['GET', 'POST'])
def loginCustomer():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Ambil token dari API
        try:
            response = requests.post('https://backend-adit-5zn7xh2gqq-et.a.run.app/loginCustomer', json={'email': email, 'password': password})
            tokenCustomer = response.json()['token']
        except Exception as e:
            print("ERROR | Get token data |", e)
            flash("Login failed", category='error')
            return redirect(url_for('loginCustomer'))
        try:
            jwt.decode(tokenCustomer, app.secret_key, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            flash("Login failed", category='error')
            return redirect(url_for('loginAdmin'))
        # Simpan email dan token pada session
        session["email"] = email
        session["token"] = tokenCustomer

        return redirect(url_for('index'))

    return render_template('loginCustomer.html')



@app.route("/registerCustomer", methods=['GET', 'POST'])
def registerCustomer():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        # kirim data ke API
        try:
            response = requests.post('https://backend-adit-5zn7xh2gqq-et.a.run.app/registercustomer',
                                     json={'name': name, 'email': email, 'password': password})

            # response status 200 = sukses
            if response.status_code == 200:
                flash("Register success", category='success')
                return redirect(url_for('loginCustomer'))
            else:
                flash("Register failed", category='error')

        except Exception as e:
            print("ERROR | Register admin |", e)
            flash("Register failed", category='error')

    return render_template('registerCustomer.html')
        































#section untuk admin dashboard
def get_admin_email():
    if 'email' in session:
        return session['email']
    return None

# untuk admin dashboard
@app.route("/dashboard", methods=['GET'])

def dashboard():
    if "email" in session and "token" in session and "role" in session:	
        # Ambil email dan token dari session
        emailAdmin = get_admin_email()
        tokenAdmin = session['token']
        role = session['role']

        # Set header Authorization dengan token JWT
        headers = {"Authorization": f"Bearer {tokenAdmin}"}
        datacountall = {}
        try:
            response = requests.get('https://backend-adit-5zn7xh2gqq-et.a.run.app/countallusers', headers=headers)
            if response.status_code == 200:
                datacountall = response.json()
                print(datacountall)
            else:
                print("ERROR | Get products data |", response.status_code)
        except Exception as e:
            print("ERROR | Get products data |", e)
        datacustomer = {}
        try:
            response = requests.get('https://backend-adit-5zn7xh2gqq-et.a.run.app/countcustomer', headers=headers)
            if response.status_code == 200:
                datacustomer = response.json()
                print(datacustomer)
            else:
                print("ERROR | Get products data |", response.status_code)
        except Exception as e:
            print("ERROR | Get products data |", e)
        
        dataadmin = {}
        try:
            response = requests.get('https://backend-adit-5zn7xh2gqq-et.a.run.app/countadmin', headers=headers)
            if response.status_code == 200:
                dataadmin = response.json()
                print(dataadmin)
            else:
                print("ERROR | Get products data |", response.status_code)
        except Exception as e:
            print("ERROR | Get products data |", e)

        dataproduct = {}
        try:
            response = requests.get('https://backend-adit-5zn7xh2gqq-et.a.run.app/countproduct', headers=headers)
            if response.status_code == 200:
                dataproduct = response.json()
                print(dataproduct)
            else:
                print("ERROR | Get products data |", response.status_code)
        except Exception as e:
            print("ERROR | Get products data |", e)

        # Tampilkan halaman index.html
        return render_template("dashboard/dashboard.html", user=emailAdmin , datacountall=datacountall, datacustomer=datacustomer, dataadmin=dataadmin, dataproduct=dataproduct, role=role)
        
    else:
        return redirect(url_for('loginAdmin'))



@app.route("/loginAdmin", methods=['GET', 'POST'])
def loginAdmin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Ambil token dari API
        try:
            response = requests.post('https://backend-adit-5zn7xh2gqq-et.a.run.app/loginAdmin', json={'email': email, 'password': password})
            tokenAdmin = response.json()['token']
            role = response.json()['role']
        except Exception as e:
            print("ERROR | Get token data |", e)
            flash("Login failed", category='error')
            return redirect(url_for('loginAdmin'))

        # Simpan email dan token pada session
        #cek token invalid
        try:
            jwt.decode(tokenAdmin, app.secret_key, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            flash("Login failed", category='error')
            return redirect(url_for('loginAdmin'))
        session["email"] = email
        session["token"] = tokenAdmin
        session["role"] = role

        return redirect(url_for('dashboard'))

    return render_template('dashboard/loginAdmin.html')


@app.route("/registerAdmin", methods=['GET', 'POST'])
def registerAdmin():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        # kirim data ke API
        try:
            response = requests.post('https://backend-adit-5zn7xh2gqq-et.a.run.app/registeradmin',
                                     json={'name': name, 'email': email, 'password': password})

            # response status 200 = sukses
            if response.status_code == 200:
                flash("Register success", category='success')
                return redirect(url_for('loginAdmin'))
            else:
                flash("Register failed", category='error')

        except Exception as e:
            print("ERROR | Register admin |", e)
            flash("Register failed", category='error')

    return render_template('dashboard/registerAdmin.html')



#read produk
#url https://frontend-adit-5zn7xh2gqq-et.a.run.app/product.html
@app.route("/product", methods=['GET', 'POST'])

def product():
    if "email" in session and "token" in session:
        # Ambil email dan token dari session
        emailCustomer = session["email"]
        tokenCustomer = session["token"]

        # Set header Authorization dengan token JWT
        headers = {"Authorization": f"Bearer {tokenCustomer}"}

        if request.method == 'POST':
            # Ambil data produk dari form
            name = request.form['name']
            description = request.form['description']
            price = request.form['price']
            stock = request.form['stock']
            

            # Buat data JSON yang berisi informasi produk yang akan ditambahkan
            data = {"name": name, "description": description, "price": price, "stock": stock }

            # Kirim request POST ke API produk
            try:
                response = requests.post('https://backend-adit-5zn7xh2gqq-et.a.run.app/addproduct', headers=headers, json=data)
                if response.status_code == 201:
                    print("Product added successfully")
                else:
                    print("ERROR | Add product |", response.status_code)
            except Exception as e:
                print("ERROR | Add product |", e)
        else:
            print("ERROR | Add product |", "Invalid request method")

        # Request ke API produk untuk mendapatkan data produk
        data = {}
        try:
            response = requests.get('https://backend-adit-5zn7xh2gqq-et.a.run.app/product' , headers=headers)
            if response.status_code == 200:
                data = response.json()
                print(data)
            else:
                print("ERROR | Get products data |", response.status_code)
        except Exception as e:
            print("ERROR | Get products data |", e)

       

        # Tampilkan halaman index.html dengan daftar produk
        return render_template("dashboard/product.html", user=emailCustomer, products=data['products'])
        
    else:
        return redirect(url_for('loginAdmin'))


@app.route("/product/delete<product_id>", methods=['GET', 'POST', 'PUT', 'DELETE'])
def delete_product(product_id):
    if "email" in session and "token" in session:
        # Ambil email dan token dari session
        emailCustomer = session["email"]
        tokenCustomer = session["token"]

        # Set header Authorization dengan token JWT
        headers = {"Authorization": f"Bearer {tokenCustomer}"}

       
        

        # Kirim request DELETE ke API produk
        try:
            response = requests.delete('https://backend-adit-5zn7xh2gqq-et.a.run.app/deleteproduct', headers=headers, json={"product_id": product_id})
            if response.status_code == 200:
                print("Product deleted successfully")
            else:
                print("ERROR | Delete product |", response.status_code)
        except Exception as e:
            print("ERROR | Delete product |", e)

        # Redirect ke halaman product setelah produk dihapus
        return redirect(url_for('product'))
    else:
        return redirect(url_for('loginAdmin'))





@app.route("/product/update<product_id>", methods=['GET', 'POST', 'PUT', 'DELETE'])
def update_product(product_id):
    if "email" in session and "token" in session:
        # Ambil email dan token dari session
        emailCustomer = session["email"]
        tokenCustomer = session["token"]

        #get data produk by id 
        headers = {"Authorization": f"Bearer {tokenCustomer}"}
        data = {}
        try:
            response = requests.post('https://backend-adit-5zn7xh2gqq-et.a.run.app/productbyid',headers=headers, json={"product_id": product_id})
            if response.status_code == 200:
                data = response.json()
                print("ini data yang di dapat dari id",data)
            else:
                print("ERROR | Get products data |", response.status_code)
        except Exception as e:
            print("ERROR | Get products data |", e)

        if request.method == 'POST':
            name = request.form['name']
            description = request.form['description']
            price = request.form['price']
            stock = request.form['stock']
            
            

            data = {"name": name, "description": description, "price": price, "stock": stock, "product_id": product_id}
            print(data)

            # Kirim request PUT ke API produk
            try:
                response = requests.put('https://backend-adit-5zn7xh2gqq-et.a.run.app/updateproduct', headers=headers, json=data)
                if response.status_code == 200:
                    print("Product update successfully")
                else:
                    print("ERROR |update product |", response.status_code)
            except Exception as e:
                print("ERROR | update product |", e)

            # Redirect ke halaman product setelah produk diubah
            return redirect(url_for('product'))
       
            

        # Set header Authorization dengan token JWT
        

        # Redirect ke halaman product setelah produk dihapus
        return render_template("dashboard/edit_product.html", user=emailCustomer, update=data)
    else:
        return redirect(url_for('loginAdmin'))



#buat order

@app.route("/product/oder<product_id>", methods=['GET', 'POST', 'PUT', 'DELETE'])
def order(product_id):
    if "email" in session and "token" in session:
        # Ambil email dan token dari session
        emailCustomer = session["email"]
        tokenCustomer = session["token"]

        # Set header Authorization dengan token JWT
        headers = {"Authorization": f"Bearer {tokenCustomer}"}

       
        
        # Kirim request DELETE ke API produk
        data = {}
        try:
            response = requests.post('https://backend-adit-5zn7xh2gqq-et.a.run.app/productbyid', headers=headers, json={"product_id": product_id})
            if response.status_code == 200:
                data = response.json()
                print("ini data yang di dapat dari id",data)
            else:
                print("ERROR | Delete product |", response.status_code)
        except Exception as e:
            print("ERROR | Delete product |", e)

        # Redirect ke halaman product setelah produk dihapus
        return render_template("cart.html", user=emailCustomer, order=data)
    else:
        return redirect(url_for('loginCustomer'))







#logout
@app.route("/logout", methods=['GET'])
def logout():
    # Hapus email dan token dari session
    session.clear()
    # Redirect ke halaman login
    return redirect(url_for('loginCustomer'))





if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=False)
