# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
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
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            break
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
# ----------------------------------------def get_available_recs(user_data):
    recommendations = []

    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            user_watched_movie = False

            for movie in user_data["watched"]:
                if friend_movie["title"] == movie["title"]:
                    user_watched_movie = True
                    break

            if user_watched_movie == False:
                if friend_movie["host"] in user_data["subscriptions"]:
                    already_added = False

                    for movie in recommendations:
                        if movie["title"] == friend_movie["title"]:
                            already_added = True
                            break

                    if already_added == False:
                        recommendations.append(friend_movie)

    return recommendations
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

