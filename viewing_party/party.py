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

    movie_dict = {}
    movie_dict["title"] = title
    movie_dict["genre"] = genre
    movie_dict["rating"] = rating

    if not title or not genre or not rating:
        return None

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

    user_data["watched"].append(movie)
                            

    if len(movie) == 0:
        movie = []

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

    if len(movie) == 0:
        movie = []

    else:
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

    return user_data

    raise ValueError(f"{title} is not on the watchlist")
    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

