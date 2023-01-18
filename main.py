from flask import jsonify, Flask, request, abort
import models
from init_db import db


app = Flask(__name__)


@app.route('/users/', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        try:
            users = db.session.query(models.User).all()
            return jsonify([user.data_user() for user in users])
        except Exception as e:
            return f"{e}"
    elif request.method == 'POST':
        data = request.json
        db.session.add(models.User(**data))
        db.session.commit()

        return jsonify(code=200)


@app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def get_user_id(user_id):
    if request.method == 'GET':
        try:
            user = db.session.query(models.User).filter(models.User.id == user_id).first()
            return jsonify(user.data_user())
        except Exception as e:
            return f"{e}"
    elif request.method == 'PUT':
        user = db.session.query(models.User).filter(models.User.id == user_id).first()

        if user is None:
            abort(404)

        db.session.query(models.User).filter(models.User.id == user_id).update(request.json)
        db.session.commit()
        return jsonify(code=200)
    elif request.method == 'DELETE':
        count = db.session.query(models.User).filter(models.User.id == user_id).delete()
        db.session.commit()
        if not count:
            abort(404)
        return jsonify(code=200)


@app.route('/orders/', methods=['GET', 'POST'])
def get_orders():
    if request.method == 'GET':
        try:
            orders = db.session.query(models.Order).all()
            return jsonify([order.get_order() for order in orders])
        except Exception as e:
            return f"{e}"
    elif request.method == 'POST':
        data = request.json
        db.session.add(models.Order(**data))
        db.session.commit()

        return jsonify(code=200)


@app.route('/orders/<int:order_id>', methods=['GET', 'PUT', 'DELETE'])
def get_order_id(order_id):
    if request.method == 'GET':
        try:
            order = db.session.query(models.Order).filter(models.Order.id == order_id).first()
            return jsonify(order.get_order())
        except Exception as e:
            return f"{e}"
    elif request.method == 'PUT':
        user = db.session.query(models.Order).filter(models.Order.id == order_id).first()

        if user is None:
            abort(404)

        db.session.query(models.Order).filter(models.Order.id == order_id).update(request.json)
        db.session.commit()
        return jsonify(code=200)
    elif request.method == 'DELETE':
        count = db.session.query(models.Order).filter(models.Order.id == order_id).delete()
        db.session.commit()
        if not count:
            abort(404)
        return jsonify(code=200)


@app.route('/offers/', methods=['GET', 'POST'])
def get_offers():
    if request.method == 'GET':
        try:
            offers = db.session.query(models.Offer).all()
            return jsonify([offer.get_offer() for offer in offers])
        except Exception as e:
            return f"{e}"
    elif request.method == 'POST':
        data = request.json
        db.session.add(models.Offer(**data))
        db.session.commit()

        return jsonify(code=200)


@app.route('/offers/<int:offer_id>', methods=['GET', 'PUT', 'DELETE'])
def get_offer_id(offer_id):
    if request.method == 'GET':
        try:
            offer = db.session.query(models.Offer).filter(models.Offer.id == offer_id).first()
            return jsonify(offer.get_offer())
        except Exception as e:
            return f"{e}"
    elif request.method == 'PUT':
        user = db.session.query(models.Offer).filter(models.Offer.id == offer_id).first()

        if user is None:
            abort(404)

        db.session.query(models.Offer).filter(models.Offer.id == offer_id).update(request.json)
        db.session.commit()
        return jsonify(code=200)
    elif request.method == 'DELETE':
        count = db.session.query(models.Offer).filter(models.Offer.id == offer_id).delete()
        db.session.commit()
        if not count:
            abort(404)
        return jsonify(code=200)


def create_app():
    app.config.from_object('config.Config')
    db.init_app(app)

    with app.app_context():
        db.create_all()

        return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=5000, debug=True)