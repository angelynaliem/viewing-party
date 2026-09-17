# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
<<<<<<< HEAD
    if title and genre and rating:
        return {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movie
    return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
=======
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


>>>>>>> f7b584897d347dfd1466867e34d990defe4487c3
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
<<<<<<< HEAD
            break
    return user_data


=======
            return user_data

    return user_data

    # raise ValueError(f"{title} is not on the watchlist")
    
>>>>>>> f7b584897d347dfd1466867e34d990defe4487c3

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
    zero_rating = 0.0
    average_rating = 0

    for movie in user_data["watched"]:
        total_rating += movie["rating"]

    if no_of_movies:
        average_rating = total_rating/no_of_movies
        return average_rating
    elif not no_of_movies:
        return zero_rating


def get_most_watched_genre(user_data):
    """
    user_data is a dictionary with "watched" list of movie dictionaries
    each movie dictionary has a key "genre"
    the value of "genre" is a string
    determine which genre is most frequently occurring in the watched list
    return the most frequently occurring genre
    if the watched list is empty, return None

    Step 1 - create a new dictionary of just the genre
    Step 2 - check the dictionary, for every 
    """

    genre_list = []
    genre_dictionary_count = {}
    highest_value = 0

    if user_data["watched"] == []:
        return None
    else:
        for movie in user_data["watched"]:
            genre_list.append(movie["genre"])
            print(genre_list)

        for genre in genre_list:
            if genre not in genre_dictionary_count:
                genre_dictionary_count[genre] = 1
            else:
                genre_dictionary_count[genre] += 1

        print(f"This is the genre dict count {genre_dictionary_count}")

        for key, value in genre_dictionary_count.items():
            if value > highest_value:
                highest_value = value
                highest_key = key

    return highest_key

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_movies = []

    for movie in user_data["watched"]:
        friend_watched_movie = False

        for friend in user_data["friends"]:
            for friend_movie in friend["watched"]:
                if movie["title"] == friend_movie["title"]:
                    friend_watched_movie = True
                    break

            if friend_watched_movie:
                break

        if friend_watched_movie == False:
            unique_movies.append(movie)

    return unique_movies
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

