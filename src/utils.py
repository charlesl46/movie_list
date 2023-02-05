from tmdbv3api import TMDb, Movie
from tqdm import tqdm
from pathlib import Path
import os
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
    for file in os.listdir('../data'):
        
        size = os.stat(f'../data/{file}').st_size / (1024**2)
        print(f'- {file} | {round(size,2)} Mo\n')

    base_name = input()
    if base_name.endswith('.txt'):
        base_name = base_name[:-4]



    filename = f'../data/{base_name}.txt'
    db = load(filename)
    return db,filename

def load(filename : str) -> DataBase:
    db = DataBase()
    db.load_movie_info(filename)
    return db


def menu(db : DataBase, filename : str) -> None:
    finished = False

    db.ajouter_Titre('Les aventures de tintin',filename=filename,addToFile=True)
    for i in tqdm(range(1,10)):
        db.ajouter_Titre(f'Star Wars',filename=filename,addToFile=True)

    print('<!> Bienvenue dans la movie database <!>\n')
    while not finished:
        print('<#> Que voulez vous faire ? <#>\n')
        print('\t - <1> Afficher la base de données active\n')
        print('\t - <2> Afficher la fiche d\' un film\n')
        print('\t - <3> Ajouter un film\n')
        print('\t - <4> Recevoir une suggestion aléatoire dans la base\n')
        print('\t - <5> Vider la base de données active\n')
        print('\t - <6> Retirer un film\n')
        print('\t - <7> Pour fermer cet utilitaire, tapez #\n')
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
            db.ajouter_Titre(titre,filename,addToFile=True)
        elif choix == '4':
            print('<!> Voici une suggestion : \n')
            print(db.sugg_Aleatoire.info)
        elif choix == '5':
            db.vider(filename = filename)
        elif choix == '6':
            print('<!> Voulez vous donner l id du film, ou son titre ?\n')
            c = input()
            if c == 'id':
                print('Quel id ?\n')
                id = str(input())
                db.retirer(filename,id)
            else:
                print('Quel titre ?\n')
                titre = str(input())
                db.retirer(titre = titre)

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
        vote_average = round(search[0].vote_average)
        the_movie = Film(title,date,overview,poster_path,vote_average)
        return the_movie,True
    else:
        # le film vide
        return Film.empty(),False

