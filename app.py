from flask import Flask, jsonify, Blueprint
import os
import json

app = Flask(__name__)
api = Blueprint('api', __name__)


def load_json(file_path):
    if not os.path.exists(file_path):
        file_path = 'error.json'
    with open(file_path, 'r') as file:
        return json.load(file)

@app.route('/')
@api.route('/')
def get_error():
    return jsonify(load_json('about.json'))


@api.route('/<endpoint>/')
def get_data(endpoint):
    filename = f"{endpoint}.json"
    print(jsonify(load_json(filename)))
    return jsonify(load_json(filename))


app.register_blueprint(api, url_prefix='/api')


if __name__ == '__main__':
    app.run(debug=False)
