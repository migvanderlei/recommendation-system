import json
from math import sqrt
from user_controller import retrieve_user_movies

DATA_FILE = 'data.json'

def reload_users():
    with open(DATA_FILE) as f:
        return json.loads(f.read())

def pearson(rating1, rating2):
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0
    n = 0
    denominator = 0
    for key in rating1:
        if key in rating2:
            n += 1
            x = rating1[key]
            y = rating2[key]
            sum_xy += x * y
            sum_x += x
            sum_y += y
            sum_x2 += pow(x, 2)
            sum_y2 += pow(y, 2)
    # now compute denominator
    if n > 0:
        denominator = sqrt(sum_x2 - pow(sum_x, 2) / n) * sqrt(sum_y2 - pow(sum_y, 2) / n)
    if denominator == 0:
        return 0
    else:
        return (sum_xy - (sum_x * sum_y) / n) / denominator
            

def computeNearestNeighbor(username, users):
    """creates a sorted list of users based on their distance to username"""

    if username in users.keys():
        distances = []
        for user in users:
            if user != username:
                distance = pearson(users[user], users[username])
                # print(distance)
                distances.append((distance, user))
        # sort based on distance -- closest first
        distances.sort()
        return distances
    
    return []

def filter_already_watched(username, recommendations):
    already_watched = retrieve_user_movies(username)

    return [
            recommendation
            for recommendation in recommendations
            if recommendation[0] not in already_watched
        ]

def recommend(username):
    """Give list of recommendations"""
    # first find nearest neighbor
    users = reload_users()
    result = computeNearestNeighbor(username, users)
    if result:
        nearest = result[0][1]

        recommendations = []
        # now find bands neighbor rated that user didn't
        neighborRatings = users[nearest]
        userRatings = users[username]
        for artist in neighborRatings:
            if not artist in userRatings:
                recommendations.append((artist, neighborRatings[artist]))
        # using the fn sorted for variety - sort is more efficient
        return sorted(recommendations, key=lambda movieTuple: movieTuple[1], reverse = True)
    return []