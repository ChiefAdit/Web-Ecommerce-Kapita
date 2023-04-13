import falcon, jwt
from datetime import datetime, timedelta, timezone
#import query order

from query.order import query_create_order


class CreateOrder:
    def on_post(self, req, resp):
        customer_email = req.media.get('customer_email')
        product_id = req.media.get('product_id')
        quantity = req.media.get('quantity')
        price = req.media.get('price')
        if not customer_email or not product_id or not quantity or not price:
            resp.status = falcon.HTTP_BAD_REQUEST
            return
        order = query_create_order(customer_email, product_id, quantity, price)
        if order is True:
            resp.status = falcon.HTTP_200
            resp.media = {'message': 'Order berhasil'}
        else:
            resp.status = falcon.HTTP_401
            resp.media = {'message': 'Order gagal'}
