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
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    for user in users_dict:
        if user['id'] == id:
            return jsonify(user)
    return {}


app.run()
