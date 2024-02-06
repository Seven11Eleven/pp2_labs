from movie_dict import movies

def compute_avg_score(movie_list):
    avg_amdb_score = sum(movie['imdb'] for movie in movie_list) / len(movie_list)
    return avg_amdb_score
print(compute_avg_score(movies))