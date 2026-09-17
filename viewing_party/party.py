# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    """
    Return None if any of the input is Falsy
    Return a dictionary if the three input are Truthy
    Title is string
    Genre is string
    Rating is float

    Step 1 - Create the dictionary with the required structure
    Step 2 - Create the conditional to return None if any input is Falsy
    """

    if not title or not genre or not rating:
        return None

    movie_dict = {}
    movie_dict["title"] = title
    movie_dict["genre"] = genre
    movie_dict["rating"] = rating

    return movie_dict

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

    Step 1 - Set `movie` as the value of `watched` by adding it to the dict list.
    Step 2 -  Create a conditional where the value of `watched` is an empty list if no movies watched.
    """

    if not movie:
        movie = []

    user_data["watched"].append(movie)
                            
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

    user_data["watchlist"].append(movie)

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

    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)

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

    Create a new dictionary of just the rating to not affect the original
    Step 1 - create a counter to track the total rating. 
    Step 2 - Divide the total with the number of movies
    """

    total_rating = 0
    no_of_movies = len(user_data["watched"])
    watched = user_data["watched"]

    if not watched:
        return 0.0

    for movie in watched:
        total_rating += movie["rating"]

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

    Step 1 - create a new dictionary of just the genre
    Step 2 - check the dictionary, for every new genre, set the count to 1. Add 1 to the count every time the loop repeats the same genre.
    Step 3 - create the tracker for highest frequency genre. Compare the tracker set at 0 with each genre's frequency. Return the highest genre.
    """

    genre_list = []
    genre_count = {}
    highest_frequency = 0
    watched = user_data["watched"]

    if not watched:
        return None
    
    for movie in watched:
        genre_list.append(movie["genre"])

        for genre in genre_list:
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
    Step 1 - Create a list of unique movies, user's movies, and friends' movies, all set as empty.
    Step 2 - Loop through the user's watched list and separately loop through the friends' watched lists to add to the corresponding empty lists.
    Step 3 - Compare the lists to see if any of the movies are not in the friends watched list, add the movies to the unique movies list.
    """

    unique_movies = []
    user_unique_movies = []
    friends_unique_movies = []

    for movie in user_data["watched"]:
        user_unique_movies.append(movie)

    for friends in user_data["friends"]:
        for friend in friends["watched"]:
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
    
    for movie in user_data["watched"]:
        user_unique_movies.append(movie)
    
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
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

    user_data = {
        
        "watched" : [{"title" : "Finding Nemo}, {"title" : "Wicked"}],
        
        "friends" : [
        {
        "watched" : [{"title" : "Wicked", "host" : "amazon prime"}, {"title" : "Mulan", "host" : "netflix"}]
        }
        ],

        "subscriptions" : ["netflix", "amazon prime"]
    
        }

    Step 1 - Create a list for recommended movies
    Step 2 - Iterate through each friend's watched movies list to see if the movies are not in the user's watched list. User the helper function above.
    Step 3 - Check if the movie's host exists in the user's subscriptions. If so, add that movie to the recommended movies list
    """

    recommended_movies = []

    friends_unique_movies = get_friends_unique_watched(user_data)
    for movie in friends_unique_movies:
        if movie["host"] in user_data["subscriptions"]:
            # Checks to makes sure the movie is not repeated if it already exists in the list
            if movie not in recommended_movies:
                recommended_movies.append(movie)

    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------



