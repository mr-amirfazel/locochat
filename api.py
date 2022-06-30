from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

import validation.signup_validation
from query_handler.blocks_utils import *
from query_handler.like_handler import *
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
from query_handler.delete_account_utils import *
from query_handler.db_users import *
from query_handler.messages_utils import *

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
        friends_list.append({'username': row[0], 'token': row[1]})
    print(friends_list)
    if len(friends) > 0:
        response = {
            'friends': friends_list
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
    if search_res is None:
        return
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
    values = request.get_json()
    username = values["username"]
    dst_username = values["dst_username"]
    remove_friends(username, dst_username)
    res = {'message': 'Unfriended with {}'.format(dst_username)}
    return jsonify(res), 200


@web_app.route('/sent_requests', methods=['POST'])
def sent_reqs():
    values = request.get_json()
    username = values["username"]
    sent_request_list = sent_requests(username)
    if sent_request_list is None:
        return
    if len(sent_request_list) == 0:
        res = {'message': 'no request found'}
        return jsonify(res), 400
    sent_list = []
    for row in sent_request_list:
        sent_list.append({'username': row[0], 'situation': row[1]})
    res = {'requests': sent_list}
    return jsonify(res), 200


@web_app.route('/received_requests', methods=['POST'])
def rec_reqs():
    values = request.get_json()
    username = values["username"]
    rc_request_list = received_requests(username)
    if rc_request_list is None:
        return
    if len(rc_request_list) == 0:
        res = {'message': 'no request found'}
        return jsonify(res), 400
    rc_list = []
    for row in rc_request_list:
        rc_list.append({'username': row[0], 'situation': row[1]})
    res = {'requests': rc_list}
    return jsonify(res), 200


@web_app.route('/blocks', methods=['POST'])
def blocks():
    values = request.get_json()
    username = values["username"]
    block_list = get_blocked_users(username)
    if block_list is None:
        return
    if len(block_list) == 0:
        res = {'message': 'no blocked users were found'}
        return res, 400
    blocked_users = []
    for row in block_list:
        blocked_users.append({'username': row[0], 'time': str(row[1])})
    res = {
        'blocks': blocked_users
    }
    return jsonify(res), 200


@web_app.route('/unblock', methods=['POST'])
def unblock():
    values = request.get_json()
    username = values["username"]
    dst_username = values["dst_username"]
    remove_blocked(username, dst_username)
    res = {'message': 'unblocked {} successfully'.format(dst_username)}
    return jsonify(res), 200


@web_app.route('/delete_account', methods=['POST'])
def delete_acc():
    values = request.get_json()
    username = values["username"]
    remove_user(username)
    res = {'message': 'user deleted account successfully'}
    return jsonify(res), 200


@web_app.route('/contacts', methods=['POST'])
def contacts():
    values = request.get_json()
    username = values["username"]
    contact_list = get_contacts({"username": username})
    if contact_list is None:
        return
    if len(contact_list) == 0:
        res = {'message': 'no chats found.....'}
        return jsonify(res), 400
    contacts_json = []
    for row in contact_list:
        if row[0] is None:
            contacts_json.append({'username': 'Deleted Account', 'token': row[1]})
        else:
            contacts_json.append({'username': row[0], 'token': row[1]})
    res = {'contacts': contacts_json}
    return jsonify(res), 200


@web_app.route('/chatroom', methods=['POST'])
def chatroom():
    values = request.get_json()
    src_username = values["src_username"]
    dst_token = values["dst_token"]
    src = get_user(src_username)
    dst = get_user_by_token(dst_token)
    print(src)
    print(dst)
    messages = get_chat(src, dst)
    if messages is None:
        return jsonify({'message': 'nothing...'}), 400
    if len(messages) == 0:
        res = {
            'message': 'no chat found'
        }
        return jsonify(res), 400
    chat_messages = []
    for row in messages:
        sender_ID = row[3]
        receiver_user_ID = row[4]
        if row[3] is None:
            sender_ID = 'Deleted Account'
        if row[4] is None:
            receiver_user_ID = 'Deleted Account'
        likes = get_liked_by(row[0])
        chat_messages.append({
            'id': row[0],
            'sender_token': row[1],
            'receiver_token': row[2],
            'sender': sender_ID,
            'receiver': receiver_user_ID,
            'message_content': row[5],
            'time': row[6],
            'seen': row[7],
            'likes': [item[0] for item in likes]
        })
    res = {'messages': chat_messages}
    return jsonify(res), 200


@web_app.route('/like', methods=['POST'])
def like():
    values = request.get_json()
    username = values["username"]
    msg_id = values['message_ID']
    like_message(username, msg_id)
    res = {'message': 'liked message by {}'.format(username)}
    return jsonify(res), 200


@web_app.route('/seen', methods=['POST'])
def set_seen():
    values = request.get_json()

    src_username = values["src_username"]
    dst_token = values["dst_token"]
    src = get_user(src_username)
    dst = get_user_by_token(dst_token)

    make_seen_message(src, dst)
    res = {'message': 'seen messages'}
    return jsonify(res), 200


@web_app.route('/send_message', methods=['POST'])
def send_msg():
    values = request.get_json()

    src_username = values["src_username"]
    dst_token = values["dst_token"]
    src = get_user(src_username)
    dst = get_user_by_token(dst_token)

    content = values["content"]
    message_obj = send_message(src, dst, content)
    sender_ID = message_obj[3]
    receiver_user_ID = message_obj[4]
    if message_obj[3] is None:
        sender_ID = 'Deleted Account'
    if message_obj[4] is None:
        receiver_user_ID = 'Deleted Account'
    likes = get_liked_by(message_obj[0])
    print(message_obj)
    res = {'message': {
        'id': message_obj[0],
        'sender_token': message_obj[1],
        'receiver_token': message_obj[2],
        'sender': sender_ID,
        'receiver': receiver_user_ID,
        'message_content': message_obj[5],
        'time': message_obj[6],
        'seen': message_obj[7],
        'likes': [item[0] for item in likes]
    }}
    return jsonify(res), 200


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=5000)
    args = parser.parse_args()
    port = args.port
    web_app.run(host='0.0.0.0', port=port)
