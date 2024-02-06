from movie_dict import movies

def avg_score_by_category(movie_list, category):
    movie_list_by_category = [movie for movie in movie_list if movie['category'] == category]
    avg_score = sum(movie['imdb'] for movie in movie_list if movie['category'] == category) / len(movie_list_by_category)
    return avg_score
print(avg_score_by_category(movies, 'Romance'))