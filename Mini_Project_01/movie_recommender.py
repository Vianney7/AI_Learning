import random

# Movie database
movies = [
    {"title": "The Matrix", "genre": "Syfy", "rating": 9.0},
    {"title": "The Avengers", "genre": "Action", "rating": 8.5},
    {"title": "The Notebook", "genre": "Romance", "rating": 7.0},
    {"title": "Avatar", "genre": "Adventure", "rating": 9.5},
    {"title": "Terminator 2", "genre": "Sci-Fi", "rating": 8.8}
]

# Filter must watch movies
def get_recommendations(min_rating):
    must_watch = []
    for movie in movies:
        if movie["rating"] >= min_rating:
            must_watch.append(movie)
    return must_watch

# Pick a random suggestion
def suggest_movie(min_rating=8.0):
    recommendations = get_recommendations(min_rating)
    suggestion = random.choice(recommendations)
    print("🎬 Tonight you should watch: " + suggestion["title"])
    print("⭐ Rating: " + str(suggestion["rating"]))
    print("🎭 Genre: " + suggestion["genre"])

# Run it!
suggest_movie()