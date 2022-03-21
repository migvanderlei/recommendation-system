from crypt import methods
import json
from flask import Flask, request
from pathlib import Path
from flask import jsonify
from recommender import recommend

DATA_PATH = str(Path(__file__).resolve().parent)
HOST = "localhost"
PORT = 5000

DEFAULT_EMPTY = {}

app = Flask(__name__)

@app.route('/recommend/<username>')
def get_recommendation(username):
    return jsonify(recommend(username))

@app.route("/user", methods = ["POST"]) # inserir um novo usuário na base
def create_user():
    user = request.form.get('username')
    if not user:
        user = request.json.get("username")

    return f"{user} OK", 200

@app.route("/review", methods=["POST"]) # inserir um novo filme
def review_movie():
    user = request.form.get('username')
    movie = request.form.get('movie')
    rating = request.form.get('rating')
    if not user:
        user = request.json.get("username")
        movie = request.json.get("movie")
        rating = request.json.get("rating")

    return "OK", 200

if __name__ == "__main__":
    # from waitress import serve

    print("Starting Recommendation Service")
    print("Listening on http://{}:{}/".format(HOST, PORT))
    print("----------------------------------------------------")

    app.run(host=HOST, port=PORT)