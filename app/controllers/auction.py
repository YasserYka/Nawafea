
from flask import request, abort, render_template
from flask import Blueprint

import datetime

from ..models.auction import Auction
from ..models.bid import Bid
from ..models.product import Product
from flask.json import jsonify

blueprint = Blueprint('auction', __name__, url_prefix='/auction')

@blueprint.route('', methods=['GET'])
def get_auctions():

    auctions = Auction.query.all()

    return render_template("auction/Auction.html", list_of_auctions=[auction.json() for auction in auctions])

@blueprint.route('<int:id>/bid', methods=['POST'])
def create_bids(id):

    auction = Auction.query.filter(Auction.id == id).one_or_none()

    if auction is None:
        abort(404)

    body = request.get_json()

    (message) = (body.get('message'))

    if message is None:
        abort(422)
        
    bid = Bid(date=datetime.datetime.now(), message=message)

    auction.bids.append(bid)

    auction.update()

    return jsonify(data=bid.json())

@blueprint.route('', methods=['POST'])
def create_auction():

    body = request.get_json()

    (description, title) = (request.form.get('description', None), request.form.get('title', None))

    if description is None or title is None:
        abort(422)

    auction = Auction(initial_bid=0, end_date=datetime.datetime.now() + datetime.timedelta(days=1), description=description, title=title)

    auction.insert()

    return jsonify(data=auction.json())

@blueprint.route('/<int:id>', methods=['DELETE'])
def delete_auction(id):

    auction = Auction.query.filter(Auction.id == id).one_or_none()

    if auction is None:
        abort(404)

    auction.delete()

    return jsonify(data=auction.json())
