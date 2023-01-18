import json

from init_db import db
from models import User, Offer, Order


def insert_data_user(input_data):
    for row in input_data:
        db.session.add(
            User(
                id=row.get("id"),
                first_name=row.get("first_name"),
                last_name=row.get("last_name"),
                age=row.get("age"),
                email=row.get("email"),
                role=row.get("role"),
                phone=row.get("phone"),
            )
        )

        db.session.commit()


def insert_data_offer(input_data):
    for row in input_data:
        db.session.add(
            Offer(
                id=row.get("id"),
                order_id=row.get("order_id"),
                executor_id=row.get("executor_id"),
            )
        )

        db.session.commit()


def insert_data_order(input_data):
    for row in input_data:
        db.session.add(
            Order(
                id=row.get("id"),
                name=row.get("name"),
                description=row.get("description"),
                start_date=row.get("start_date"),
                end_date=row.get("end_date"),
                address=row.get("address"),
                price=row.get("price"),
                customer_id=row.get("customer_id"),
                executor_id=row.get("executor_id"),
            )
        )

        db.session.commit()


def data_to_db():
    db.drop_all()
    db.create_all()

    with open("data/user.json") as file:
        insert_data_user(json.load(file))

    with open("data/offer.json") as file:
        insert_data_offer(json.load(file))

    with open("data/order.json") as file:
        insert_data_order(json.load(file))
