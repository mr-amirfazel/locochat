from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

import validation.signup_validation
from store import store
from validation import *
from validation import signup_validation
from query_handler import sign_up

Store = store()

web_app = Flask(__name__)
CORS(web_app)


@web_app.route('/signup', methods=['POST'])
def signup():
    values = request.get_json()
    print(values)
    validity = signup_validation.valid_user(values)
    if validity:
        sign_up.sign_up(values)
        response = {
            'message': 'user signed up successfully'
        }
        return jsonify(response), 200
    response = {
        'message': 'failed to sign up',
        'error': Store.signup_error_message
    }
    return jsonify(response), 400


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=5000)
    args = parser.parse_args()
    port = args.port
    web_app.run(host='0.0.0.0', port=port)
