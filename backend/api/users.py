import falcon, jwt
from datetime import datetime, timedelta, timezone


from query.users import query_login_admin, query_login_customer, query_register, query_register_admin, query_get_all_users, query_get_user_by_email, query_update_user_by_email, query_delete_user_by_email,  query_count_admin, query_count_users, query_count_all_users

class LoginResourceAdmin:
   def on_post(self, req, resp):
      email = req.media.get('email')
      password = req.media.get('password')
      if not email or not password:
         resp.status = falcon.HTTP_BAD_REQUEST
         return
      admin = query_login_admin(email, password)
      if admin:
         token = jwt.encode({'email': email, 'exp': datetime.utcnow() + timedelta(minutes=30)}, 'secretkey', algorithm='HS256')
         resp.media = {'token': token, 'role': 'admin'}
         resp.status = falcon.HTTP_200
      else:
         resp.status = falcon.HTTP_401
         resp.media = {'message': 'Email atau password salah'}

class LoginResourceCustomer:
   def on_post(self, req, resp):
      email = req.media.get('email')
      password = req.media.get('password')
      if not email or not password:
         resp.status = falcon.HTTP_BAD_REQUEST
         return
      customer = query_login_customer(email, password)
      if customer:
         token = jwt.encode({'email': email, 'exp': datetime.utcnow() + timedelta(minutes=30)}, 'secretkey', algorithm='HS256')
         resp.media = {'token': token}
         resp.status = falcon.HTTP_200
      else:
         resp.status = falcon.HTTP_401
         resp.media = {'message': 'Email atau password salah'}

class RegisterResourceCus:
   def on_post(self, req, resp):
      email = req.media.get('email')
      password = req.media.get('password')
      name = req.media.get('name')
      if not email or not password or not name:
         resp.status = falcon.HTTP_BAD_REQUEST
         return
      user = query_register(email, password, name)
      if user is True:
         resp.status = falcon.HTTP_200
         resp.media = {'message': 'Register customer berhasil '}
      else:
         resp.status = falcon.HTTP_401
         resp.media = {'message': 'register customer gagal'}

class RegisterResourceAdmin:
   def on_post(self, req, resp):
      email = req.media.get('email')
      password = req.media.get('password')
      name = req.media.get('name')
      if not email or not password or not name:
         resp.status = falcon.HTTP_BAD_REQUEST
         return
      user = query_register_admin(email, password, name)
      if user is True:
         resp.status = falcon.HTTP_200 
         resp.media = {'message': 'Register admin berhasil'}
      else:
         resp.status = falcon.HTTP_401
         resp.media = {'message': 'register admin gagal'}

class CountAllUsersResource:
   def on_get(self, req, resp):
      users = query_count_all_users()
      if users:
         resp.status = falcon.HTTP_200
         resp.media = users
      else:
         resp.status = falcon.HTTP_404
         resp.media = {'message': 'Tidak ada user'}


class CountUserAdmin:
   def on_get(self, req, resp):
      users = query_count_admin()
      if users:
         resp.status = falcon.HTTP_200
         resp.media = users
      else:
         resp.status = falcon.HTTP_404
         resp.media = {'message': 'Tidak ada user'}

class CountUserCustomer:
   def on_get(self, req, resp):
      users = query_count_users()
      if users:
         resp.status = falcon.HTTP_200
         resp.media = users
      else:
         resp.status = falcon.HTTP_404
         resp.media = {'message': 'Tidak ada user'}







"""
app = falcon.API()
app.add_route('/login', LoginResource())
app.add_route('/register', RegisterResource())
app.add_route('/users', GetAllUsersResource())
app.add_route('/users/{user_id}', GetUserByIdResource())
app.add_route('/users/{user_id}', UpdateUserByIdResource())
app.add_route('/users/{user_id}', DeleteUserByIdResource())

if __name__ == '__main__':
   serve(app, host='0.0.0.0', port=8000)
   """