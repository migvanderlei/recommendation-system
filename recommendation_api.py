from crypt import methods
import json
from flask import Flask, request
from pathlib import Path
from flask import jsonify
from recommender import recommend
from user_controller import insert_user, create_review, retrieve_movies_list

DATA_PATH = str(Path(__file__).resolve().parent)
HOST = "localhost"
PORT = 5000

DEFAULT_EMPTY = {}

app = Flask(__name__)

@app.route('/movies')
def get_movies():
    return jsonify(retrieve_movies_list())

@app.route('/recommend/<username>')
def get_recommendation(username):
    return jsonify(recommend(username))

@app.route("/user", methods = ["POST"]) # inserir um novo usuário na base
def create_user():
    username = request.form.get(
        'username',
        request.json.get("username")
        )
    
    if not username:
        return "username is required", 400

    status, msg = insert_user(username)

    if status:
        return msg, 200
    else:
        return msg, 404

@app.route("/review", methods=["POST"]) # inserir um novo filme
def review_movie():
    username = request.form.get(
        'username',
        request.json.get("username")
        )
    movie = request.form.get(
        'movie',
        request.json.get("movie")
        )
    rating = request.form.get(
        'rating',
        request.json.get("rating")
        )
    if not username or not movie or not rating:
        return "one of the required fields (username, movie, rating) is missing", 400

    status, msg = create_review(username, movie, rating)

    if status:
        return msg, 200
    else:
        return msg, 404

if __name__ == "__main__":
    # from waitress import serve

    print("Starting Recommendation Service")
    print("Listening on http://{}:{}/".format(HOST, PORT))
    print("----------------------------------------------------")

    app.run(host=HOST, port=PORT)