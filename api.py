from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

import validation.signup_validation
from query_handler.blocks_utils import *
from validation import login_validation
from store import store
from validation import *
from validation import signup_validation
from query_handler import sign_up
from query_handler.log_in import log_in
from query_handler.log_out import log_out
from query_handler.logged_in_user import check_login
from query_handler.friends_utils import *
from query_handler.search import *
from query_handler.friend_request_utils import *

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


@web_app.route('/login', methods=['POST'])
def login():
    values = request.get_json()
    print(values)
    validity = login_validation.valid_entry(values)
    if validity["validity"]:
        log_in(values)
        response = {
            'message': 'user logged in successfully'
        }
        return jsonify(response), 200
    response = {
        'message': 'failed to login',
        'error': validity["message"]
    }
    return jsonify(response), 400


@web_app.route('/logout', methods=['POST'])
def logout():
    values = request.get_json()
    log_out(values)
    response = {
        'message': 'Logged out'
    }
    return jsonify(response), 200


@web_app.route('/logged_user', methods=['GET'])
def logged_in_user():
    count, user = check_login()
    if count:
        response = {
            'username': user["username"]
        }
        return response, 200
    response = {
        'message': 'no user is logged in'
    }
    return response, 400


@web_app.route('/friends', methods=['POST'])
def get_friends_list():
    values = request.get_json()
    friends = get_friends(values["username"])
    friends_list = []
    for row in friends:
        friends_list.append(row[0])
    print(friends_list)
    friends = [{"username": friend} for friend in friends_list]
    print(friends)
    if len(friends) > 0:
        response = {
            'friends': friends
        }
        return jsonify(response), 200
    response = {
        'message': 'no friends found'
    }
    return jsonify(response), 400


@web_app.route('/search', methods=['POST'])
def search_for_user():
    values = request.get_json()
    print(values["username"])
    search_res = search(values["username"])
    print(search_res)
    if len(search_res) == 0:
        response = {
            'message': 'no User found'
        }
        return jsonify(response), 400
    result = []
    for row in search_res:
        result.append(row[0])
    users = [{'username': res} for res in result]
    response = {
        'users': users
    }
    return jsonify(response), 200


@web_app.route('/add_friend', methods=['POST'])
def add_friend():
    values = request.get_json()
    username = values["username"]
    dst_username = values["dst_username"]
    if has_blocked(username, dst_username):
        res = {'message': 'you have blocked {} you have to unblock this user first'.format(dst_username)}
        return jsonify(res), 400
    if has_blocked(dst_username, username):
        res = {'message': 'Since you have been blocked by {}, you cant send a friendship request to this user'.format(
            dst_username)}
        return jsonify(res), 400
    if is_friend(username, dst_username):
        res = {'message': 'You are already a friend of {}'.format(dst_username)}
        return jsonify(res), 400
    if request_exists(username, dst_username):
        res = {'message': 'A request had already been sent to {}'.format(dst_username)}
        return jsonify(res), 400
    if reverse_request(username, dst_username):
        res = {
            'message': 'A request had already been sent from {} to you. You can go and accept it'.format(dst_username)}
        return jsonify(res), 400
    send_request(username, dst_username)
    res = {
        'message': 'successfully sent friend request to {} '.format(dst_username)
    }
    return jsonify(res), 200


@web_app.route('/block', methods=['POST'])
def block():
    values = request.get_json()
    username = values["username"]
    dst_username = values["dst_username"]

    if has_blocked(username, dst_username):
        res = {'message': 'you already have blocked user with username: {}'.format(dst_username)}
        return jsonify(res), 400
    if is_friend(username, dst_username):
        remove_friends(username, dst_username)

    block_user(username, dst_username)
    res = {'message': 'successfully blocked {}'.format(dst_username)}
    return jsonify(res), 200


@web_app.route('/unfriend', methods=['POST'])
def unfriend():
    print('arrrrrrrrrrrr')
    values = request.get_json()
    username = values["username"]
    dst_username = values["dst_username"]
    remove_friends(username, dst_username)
    res = {'message': 'Unfriended with {}'.format(dst_username)}
    return jsonify(res), 200


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=5000)
    args = parser.parse_args()
    port = args.port
    web_app.run(host='0.0.0.0', port=port)
