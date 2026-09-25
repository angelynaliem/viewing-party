# ------------- WAVE 1 --------------------

KEY_MOVIE_TITLE = "title"
KEY_MOVIE_GENRE = "genre"
KEY_MOVIE_RATING = "rating"
KEY_MOVIE_WATCHED = "watched"
KEY_MOVIE_WATCHLIST = "watchlist"
KEY_MOVIE_FRIENDS = "friends"
KEY_MOVIE_HOST = "host"
KEY_MOVIE_SUBSCRIPTIONS = "subscriptions"
KEY_MOVIE_FAVORITES = "favorites"

def create_movie(title, genre, rating):
    """
    Return None if any of the input is Falsy
    Return a dictionary if the three input are Truthy
    Title is string
    Genre is string
    Rating is float
    """

    if not title or not genre or not rating:
        return None

    return {
        KEY_MOVIE_TITLE : title,
        KEY_MOVIE_GENRE : genre,
        KEY_MOVIE_RATING : rating,
    }

def add_to_watched(user_data, movie):
    """
    user_data is a dictionary. Key = "watched" Value = a list of dictionaries representing the movies the user has watched
    Note: an empty list = the user has no movies in their watched list
    movie is a dictionary with the format:
    on
    {
        "title": "Title A",
        "genre": "Horror",
        "rating": 3.5
    }
    Add the `movie` to the "watched" list inside the user_data
    Return the user_data
    """

    if not movie:
        movie = []

    user_data[KEY_MOVIE_WATCHED].append(movie)
                            
    return user_data

def add_to_watchlist(user_data, movie):
    """
    user_data is a dictionary. Key = "watchlist" Value = a list of dictionaries that the user wants to watch
    If the user has no movies in the watchlist, the value is an empty list
    movie is a dictionary with the format:
    {
        "title": "Title A",
        "genre": "Horror",
        "rating": 3.5
    }
    Add the `movie` to the "watchlist" inside the user_data
    Return the user_data
    """

    if not movie:
        movie = []

    user_data[KEY_MOVIE_WATCHLIST].append(movie)

    return user_data

def watch_movie(user_data, title):
    """
    user_data is a dictionary. Keys = "watchlist" and "watched"
    The value of "watchlist" is a List.
    The value of "watched" is also a List.
    title = string, title of movie the user has watched
    If the title is in the "watchlist": 
    1. Remove the movie from the "watchlist"
    2. Add the movie to "watched"
    Return the user_data
    If the title is not a movie in the "watchlist":
    1. Return the user_data
    """

    for movie in user_data[KEY_MOVIE_WATCHLIST]:
        if movie[KEY_MOVIE_TITLE] == title:
            user_data[KEY_MOVIE_WATCHLIST].remove(movie)
            user_data[KEY_MOVIE_WATCHED].append(movie)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    """
    user_data is a dictionary with a "watched" list of movie dictionaries
    calculate the average rating of all movies in the watched list
    the average rating of an empty watched list is 0.0 (float)
    return the average rating
    """

    total_rating = 0
    no_of_movies = len(user_data[KEY_MOVIE_WATCHED])
    watched = user_data[KEY_MOVIE_WATCHED]

    if not watched:
        return 0.0

    for movie in watched:
        total_rating += movie[KEY_MOVIE_RATING]

    average_rating = total_rating/no_of_movies

    return average_rating


def get_most_watched_genre(user_data):
    """
    user_data is a dictionary with "watched" list of movie dictionaries
    each movie dictionary has a key "genre"
    the value of "genre" is a string
    determine which genre is most frequently occurring in the watched list
    return the most frequently occurring genre
    if the watched list is empty, return None
    """

    genre_count = {}
    highest_frequency = 0
    highest_genre = None
    watched = user_data[KEY_MOVIE_WATCHED]

    if not watched:
        return None
    
    for movie in watched:
        genre = movie[KEY_MOVIE_GENRE]
        if genre not in genre_count:
            genre_count[genre] = 1
        else:
            genre_count[genre] += 1

    for genre, frequency in genre_count.items():
        if frequency > highest_frequency:
            highest_frequency = frequency
            highest_genre = genre

    return highest_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    """
    user_data is a dictionary with a "watched" list of movie dictionaries, and a "friends" list
    each item in the friends list is a dictionary
    each movie dictionary has a "title"
    Return a list of dictionaries that represents a list of movies that the user has watched, but the friends have not.
    
    user_data = {
    
    "watched" : [{"title" : "Finding Nemo}, {"title" : "Wicked"}],
    
    "friends" : [
    {
    "watched" : [{"title" : "Wicked"}, {"title" : "Mulan"}]
    }
    ]

    }
    """

    unique_movies = []
    user_unique_movies = []
    friends_unique_movies = []

    for movie in user_data[KEY_MOVIE_WATCHED]:
        user_unique_movies.append(movie)

    for friends in user_data[KEY_MOVIE_FRIENDS]:
        for friend in friends[KEY_MOVIE_WATCHED]:
            friends_unique_movies.append(friend)

    for user_movie in user_unique_movies:
        if user_movie not in friends_unique_movies:
            unique_movies.append(user_movie)

    return unique_movies
    
            
def get_friends_unique_watched(user_data):
    """
    user_data has the same structure as previous function
    find out a movie in the friends list that the user has not watched
    return a list of movies that the user has not watched that the friend/s have
    """
    unique_movies = []
    user_unique_movies = []
    friends_unique_movies = []
    
    for movie in user_data[KEY_MOVIE_WATCHED]:
        user_unique_movies.append(movie)
    
    for friend in user_data[KEY_MOVIE_FRIENDS]:
        for movie in friend[KEY_MOVIE_WATCHED]:
            friends_unique_movies.append(movie)
    
    for friend_movie in friends_unique_movies:
        if friend_movie not in user_unique_movies:
            # Checks to make sure the movie is not repeated in the unique_movies list
            if friend_movie not in unique_movies:
                unique_movies.append(friend_movie)
    
    return unique_movies
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    """
    user_data has a key "subscriptions"
    the value of "subscriptions" is a list of strings
    for each friend, each movie has a key "host"
    the value of "host" is a string

    return a list of recommended movies
    criteria for the recommended movie:
    - user has not watched it
    - a friend has watched it
    - the "host" of the movie is a service in the user's "subscriptions"
    """

    recommended_movies = []

    friends_unique_movies = get_friends_unique_watched(user_data)
    for movie in friends_unique_movies:
        if movie[KEY_MOVIE_HOST] in user_data[KEY_MOVIE_SUBSCRIPTIONS]:
            # Checks to makes sure the movie is not repeated if it already exists in the list
            if movie not in recommended_movies:
                recommended_movies.append(movie)

    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    recommendation = []

    most_frequently_watched_genre = get_most_watched_genre(user_data) # A string which is the genre, e.g. "Horror"
    
    friend_movie = get_friends_unique_watched(user_data) # A list of friends' movies the user has not watched

    if not user_data[KEY_MOVIE_WATCHED]:
        return recommendation
    
    for movie in friend_movie:
        if movie[KEY_MOVIE_GENRE] == most_frequently_watched_genre:
            recommendation.append(movie)
        
    return recommendation

def get_rec_from_favorites(user_data):
    """
    user_data has a new key called "favorites". The value of "favorites" is a list of the user's favorite movies
    create a new list of recommended movies for the friends
    add a movie to the list for friends if:
    - the movie is in "favorites"
    - friends have not watched it
    return the list for friends
    """
    
    recommendations = []
    
    all_watched_movies_in_friends = []
    
    for friend in user_data[KEY_MOVIE_FRIENDS]:
        for friend_movie in friend[KEY_MOVIE_WATCHED]:
            all_watched_movies_in_friends.append(friend_movie)


    for movie in user_data[KEY_MOVIE_FAVORITES]:
        if movie not in all_watched_movies_in_friends:
            recommendations.append(movie)
    
    return recommendations