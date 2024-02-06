from movie_dict import movies


def filter_movies_by_score(movie_list):
    high_score_movies = [movie for movie in movie_list if movie['imdb'] > 5.5]
    return high_score_movies


print(filter_movies_by_score(movies))
