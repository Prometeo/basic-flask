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


app.run()
