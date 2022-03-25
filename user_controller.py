import json

DATA_FILE = 'data.json'
MOVIES_FILE = 'movies.txt'

def reload_users():
    with open(DATA_FILE) as f:
        return json.loads(f.read())


def insert_user(username):
    users = reload_users()
    
    if users.get(username):
        return False, "username already exists"
    else:
        users[username] = {}
        with open(DATA_FILE, 'w') as f:
            f.write(json.dumps(users))
        
        return True, f"username {username} created successfully"

def create_review(username, movie, rating):
    users = reload_users()

    user_ratings = users.get(username)

    if user_ratings is not None:
        if user_ratings.get(movie):
            old_rating = user_ratings[movie]
            user_ratings[movie] = rating

            msg = f"movie \"{movie}\" rating updated from {old_rating} to {rating}"
        else:
            user_ratings[movie] = rating

            msg = f"movie \"{movie}\" rated with {rating}"

        users[username] = user_ratings

        with open(DATA_FILE, 'w') as f:
            f.write(json.dumps(users))
        
        update_movies_list(movie)

        return True, msg
        
    return False, "username does not exist"

def retrieve_user_movies(username):
    users = reload_users()

    user_ratings = users.get(username)

    return set(user_ratings.keys())

def retrieve_movies_list():
    with open(MOVIES_FILE) as f:
        return f.read().split('\n')

def update_movies_list(movie):
    movies = set(retrieve_movies_list())

    if movie not in movies:
        movies.add(movie)

        movies_list = '\n'.join(movies)
        
        with open(MOVIES_FILE, 'w') as f:
            f.write(movies_list)

