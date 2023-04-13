import falcon, jwt
import json
import psycopg2
from waitress import serve
from connectdb import conn

from api.users import LoginResourceAdmin, LoginResourceCustomer, RegisterResourceCus, RegisterResourceAdmin, CountAllUsersResource, CountUserAdmin, CountUserCustomer
from api.product import ReadProduct, AddProduct, Updateproduct, DeleteProduct, GetProductById, CountProduct
from api.order import CreateOrder




# buat middleware jika ingin mengakses halaman harus login terlebih dahulu
 



# Inisialisasi aplikasi Falcon
app = falcon.API()

# Tambahkan route untuk login dan halaman terproteksi
app.add_route('/loginAdmin', LoginResourceAdmin())
app.add_route('/loginCustomer', LoginResourceCustomer())
#app.add_route('/protected', ProtectedResource())
app.add_route('/registercustomer', RegisterResourceCus())
app.add_route('/registeradmin', RegisterResourceAdmin())
app.add_route('/countallusers', CountAllUsersResource())
app.add_route('/countadmin', CountUserAdmin())
app.add_route('/countcustomer', CountUserCustomer())




app.add_route('/product', ReadProduct())
app.add_route('/addproduct', AddProduct())
app.add_route('/updateproduct', Updateproduct())
app.add_route('/deleteproduct', DeleteProduct())
app.add_route('/productbyid', GetProductById())
app.add_route('/countproduct', CountProduct())


#order
app.add_route('/createorder', CreateOrder())

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)
