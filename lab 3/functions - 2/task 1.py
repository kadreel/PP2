movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

def isGood(movie):                                          #gets the IMDb out of the name
    global curIMDB
    curIMDB = movie["imdb"]                                 #gets imdb for no reason rly
    return movie["imdb"] > 5.5                              #good stuff

def imdb(movie_name):
    for movie in movies:
        if movie["name"].lower() == movie_name.lower():     #checks if it exists and accounts for UPPERCASE and lowercase
            return isGood(movie)
    return "Not found"

curIMDB = "N/A"                                             #just in case
movie_name = input("Pick a movie: ")                        #input name of desired movie

print(f"{imdb(movie_name)}, IMDb rating is {curIMDB}")      #assuming input is "Love", the output is "True, IMDb rating is 6.0". For "exam", it's "False, IMDb rating is 4.2"