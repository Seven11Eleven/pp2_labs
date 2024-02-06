from movie_dict import movies

def all_movies_under_category(category):
    return [movie for movie in movies if movie['category'] == category]

print(all_movies_under_category('Romance'))