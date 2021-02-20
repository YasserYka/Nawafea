
from flask import request, abort, render_template
from flask import Blueprint

import datetime

from ..models.product import Product
from ..models.purchase import Purchase
from flask.json import jsonify
from ..models.auction import Auction

blueprint = Blueprint('product', __name__, url_prefix='/product')

@blueprint.route('', methods=['GET'])
def get_products():

    products = Product.query.all()

    if len(products) == 0:
        abort(404)

    return jsonify(data=[product.json() for product in products])

@blueprint.route('/<int:id>/purchasenow', methods=['POST'])
def purchase_product(id):

    body = request.get_json()

    (products) = (body.get('products'))

    if products is None:
        abort(422)

    total = 0
    purchase = Purchase(datetime.datetime.now())

    for product in products:
        product = Product.query.filter(Product.id == product).one_or_none()

        if product is None:
            abort(422)
        
        if not product.sold:
            purchase.total += product.price
            product.sold = True
            purchase.products.append(product)

    purchase.insert()

    return render_template("auction/Auction.html", list_of_auctions=[auction.json() for auction in auctions])

@blueprint.route('', methods=['POST'])
def create_product():

    body = request.get_json()

    name = request.form.get('name', None)
    description = request.form.get('description', None)
    price = request.form.get('price', None)
    supiler_name = request.form.get('supiler_name')

    if name is None or description is None or price is None or supiler_name is None:
        abort(422)

    product = Product(name=name, price=price, description=description, supiler_name=supiler_name)

    if  'file' in request.files: 
        img = request.files['file']

        product.image = img.read()
        product.imagename = img.filename

    product.insert()

    auction = Auction(initial_bid=0, end_date=datetime.datetime.now() + datetime.timedelta(days=1), description=description, title=name)

    auction.products.append(product)

    auction.insert()

    return jsonify(data=product.json())


@blueprint.route('/<int:id>', methods=['PATCH'])
def update_product(id):

    product = Product.query.filter(Product.id == id).one_or_none()

    if product is None:
        abort(404)

    body = request.get_json()

    (name, description, price) = (body.get('name'), body.get('description'), body.get('price'))

    if name is not None:
        product.name = name

    if description is not None:
        product.description = description

    if 'file' in request.files:
        img = request.files['file']
        product.image = img.read()

    product.update()

    return jsonify(data=product.json())


@blueprint.route('/<int:id>', methods=['DELETE'])
def delete_product(id):

    product = Product.query.filter(Product.id == id).one_or_none()

    if product is None:
        abort(404)

    product.delete()

    return jsonify(data=product.json())

