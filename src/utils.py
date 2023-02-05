from tmdbv3api import TMDb, Movie
import urllib.request
import time
from Film import Film
from DataBase import DataBase


def init() -> DataBase:
    """Une fonction pour initialiser l'accès à l'API de TMBD"""
    tmdb = TMDb()
    tmdb.api_key = 'a5beed50b62bc4886b8da6bb2b823fa3'
    tmdb.language = 'fr'
    tmdb.debug = True

    print('<!> Quelle base lire ? <!>\n')
    base = input()
    db = load(base)
    return db

def load(base : str) -> DataBase:
    filename = f'../data/{base}.txt'
    db = DataBase()
    db.load_movie_info(filename)
    return db


def menu(db : DataBase) -> None:
    finished = False
    print('<!> Bienvenue dans la movie database <!>\n')
    while not finished:
        print('<#> Que voulez vous faire ? <#>\n')
        print('\t - <1> Afficher la base de données\n')
        print('\t - <2> Afficher la fiche d\' un film\n')
        print('\t - <3> Ajouter un film\n')
        print('\t - <4> Recevoir une suggestion aléatoire dans la base\n')
        print('\t - <5> Pour fermer cet utilitaire, tapez #\n')
        choix = input()
        if choix == '#':
            finished = True
        elif choix == '1':
            db.afficher()
        elif choix == '2':
            print('<!> Quel film (id)?\n')
            id = input()
            print(db._movie_list[id].info)
        elif choix == '3':
            print('<!> Quel film (titre)?\n')
            titre = input()
            db.ajouter_Titre(titre)

    print('</o\> Merci de votre visite')

        


def retrieve_movie_info(titre : str):
    """Une fonction pour récupérer les infos d'un film"""
    movie = Movie()
    search = movie.search(titre)
    if len(search) != 0:
        title = search[0].title
        date = search[0].release_date
        overview = search[0].overview
        poster_path = search[0].poster_path
        vote_average = search[0].vote_average
        the_movie = Film(title,date,overview,poster_path,vote_average)
        return the_movie,True
    else:
        # le film vide
        return Film.empty(),False

