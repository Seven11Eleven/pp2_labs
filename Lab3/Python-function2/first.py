from movie_dict import movies

def score_above(movies):
    return movies['imdb'] > 5.5
print(score_above(movies[7]))