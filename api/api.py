import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# Users dictionary
users_dict = [{'id': 1, 'name': 'Kunka', 'age': 30},
              {'id': 2, 'name': 'pudge', 'age': 25}]


@app.route('/', methods=['GET'])
def home():
    return jsonify(users_dict)


@app.route('/user', methods=['GET'])
def get_user_by_id():
    # get parameter 'id' from request
    """ http://127.0.0.1:5000/user?id=1 """
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    for user in users_dict:
        if user['id'] == id:
            return jsonify(user)

    return {}


@app.route('/user/<id>', methods=['GET'])
def get_user_by_id_in_path(id):
    """ http://127.0.0.1:5000/user/1"""
    for user in users_dict:
        if user['id'] == int(id):
            return jsonify(user)

    return {}


@app.route('/user', methods=['POST'])
def post_users():
    user = request.get_json()
    user['id'] = len(users_dict) + 1
    users_dict.append(user)
    return jsonify(user)


@app.route('/users', methods=['GET'])
def get_users():
    """ 127.0.0.1:5000/users?name=pudge 
        127.0.0.1:5000/users?name=pudGE&id=2
        127.0.0.1:5000/users?age=25
    """
    users = []
    for user in users_dict:
        countProp = 0
        for arg in request.args:
            val = user[arg]
            param = request.args[arg]
            if isinstance(val, int):
                param = int(param)
            if isinstance(val, str):
                val = val.upper()
                param = param.upper()
            if val == param:
                countProp += 1
        if countProp == len(request.args):
            users.append(user)
    return jsonify(users)


@app.route('/user', methods=['PUT'])
def put_users():
    user = request.get_json()
    for i, u in enumerate(users_dict):
        if u['id'] == user['id']:
            users_dict[i] = user
    return {}


@app.route('/user/<id>', methods=['DELETE'])
def delete_useres(id):
    for user in users_dict:
        if user['id'] == int(id):
            users_dict.remove(user)
    return {}


app.run()
