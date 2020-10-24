from flask import Flask, send_from_directory, jsonify, Response, request
import os
import stripe
import json
import sys

import datetime as dt
from datetime import datetime

root_dir = os.path.abspath(os.path.dirname(__file__))
build_dir = os.path.abspath(os.path.join(root_dir, '..', 'build'))

app = Flask(__name__, static_url_path=build_dir, static_folder='')

stripe.api_key = 'sk_test_51HeNvWCnovgGvFVaUhFJFjwylH37MKyGa6pxeoGx5VMGyxGzl0Tf3Uw5njIBT8LJbNUAtGVumirbGz72uvCnSkUq000WkHgFPK'

@app.route('/')
def root():
    return send_from_directory('../build', 'index.html')

@app.route('/create-payment-intent')
def create_payment_intent():
    intent = stripe.PaymentIntent.create(
        amount=10000,
        currency='usd',
        metadata={'integration_check': 'accept_a_payment'}
    )
    return jsonify(client_secret=intent.client_secret)

@app.route('/log-payment', methods=['POST'])
def log_payment():
    payload = request.json
    event = None

    try:
        event = stripe.Event.construct_from(
            payload, stripe.api_key
        )
    except ValueError as e:
        return Responses(status=400)

    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object
        log_payment_to_file(payment_intent)
    
    return Response(status=200)

def log_payment_to_file(payment):

    with open('payment_log.txt', 'a') as f:
        f.write("$" + str(payment.amount) + ", " +
                datetime.fromtimestamp(payment.created).strftime('%Y-%m-%d %H:%M:%S') + ", " +
                payment.shipping.name + ", " + payment.shipping.address.line1 + ", " +
                payment.shipping.address.city + ", " + payment.shipping.address.state +
                " " + payment.shipping.address.postal_code + "\n")

@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('../build', path)


if __name__ == "__main__":
    app.run()
