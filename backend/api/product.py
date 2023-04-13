import falcon, jwt
from datetime import datetime, timedelta, timezone


from query.product import query_get_all_products, query_add_product, query_delete_product, query_update_product, query_get_product_by_id, query_count_product
class ReadProduct:
    def on_get(self, req, resp):
        products = query_get_all_products()
        if products:
            resp.media = {"products": products}
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_404
            resp.media = {'message': 'Product not found'}

class AddProduct:
    def on_post(self, req, resp):
        name = req.media.get('name')
        description = req.media.get('description')
        price = req.media.get('price')
        stock = req.media.get('stock')
        
        if not name or not description or not price or not stock :
            resp.status = falcon.HTTP_BAD_REQUEST
            return
        product = query_add_product(name, description, price, stock)
        if product is True:
            resp.status = falcon.HTTP_200
            resp.media = {'message': 'Add product berhasil'}
        else:
            resp.status = falcon.HTTP_401
            resp.media = {'message': 'Add product gagal'}


class DeleteProduct:
    def on_delete(self, req, resp):
        name = req.media.get('product_id')
        if not name:
            resp.status = falcon.HTTP_BAD_REQUEST
            return
        product = query_delete_product(name)
        if product is True:
            resp.status = falcon.HTTP_200
            resp.media = {'message': 'Delete product berhasil'}
        else:
            resp.status = falcon.HTTP_401
            resp.media = {'message': 'Delete product gagal'}

class Updateproduct :
    def on_put(self, req, resp):
        name = req.media.get('name')
        description = req.media.get('description')
        price = req.media.get('price')
        stock = req.media.get('stock') 
        product_id = req.media.get('product_id')
        if not name or not description or not price or not stock:
            resp.status = falcon.HTTP_BAD_REQUEST
            return
        product = query_update_product(name, description, price, stock,  product_id)
        if product is True:
            resp.status = falcon.HTTP_200
            resp.media = {'message': 'Update product berhasil'}
        else:
            resp.status = falcon.HTTP_401
            resp.media = {'message': 'Update product gagal'}

class GetProductById:
    def on_post(self, req, resp):
        product_id = req.media.get('product_id')
        if not id:
            resp.status = falcon.HTTP_BAD_REQUEST
            return
        product = query_get_product_by_id(product_id)
        if product:
            resp.status = falcon.HTTP_200
            resp.media = { "product": product}
        else:
            resp.status = falcon.HTTP_401
            resp.media = {'message': 'Product not found'}
        
class CountProduct:
    def on_get(self, req, resp):
        product = query_count_product()
        if product:
            resp.status = falcon.HTTP_200
            resp.media = product
        else:
            resp.status = falcon.HTTP_401
            resp.media = {'message': 'Product not found'}