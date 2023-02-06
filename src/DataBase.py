"""A module to modelize a Movie DataBase"""

from tmdbv3api import TMDb, Movie
from Film import Film
from tqdm import tqdm
import random

class DataBase:
    """Une classe permettant de gérer une base de données de Classes Film"""
    def __init__(self) -> None:
        movie_list = {}
        self._movie_list = movie_list
        self._length = 0
        pass

    
    def vider(self,filename : str) -> None:
        """Une fonction permettant de vider la base de données

        Args:
            filename (str): le nom du fichier qui contient la base de données
        """

        file = open(filename, 'w').close()
        self._movie_list.clear()
        self._length = 0

    def load_movie_info(self,filename : str):
        file = open(filename,'r')
        inLoop = False
        print('<!> Loading ...\n')
        nb_films_file = 0
        for line in tqdm(file):

            if inLoop:
                count = count - 1
                if count == 3:
                    film.definirTitre(line)
                elif count == 2:
                    film.definirDate(line)
                elif count == 1:
                    film.definirOverview(line)
                elif count == 0:
                    film.definirVote(line)
                    self.ajouter_Film(film,filename,addToFile = False)

                    inLoop = False
            else:
                nb_films_file += 1
                film = Film.empty()
                inLoop = True
                count = 4
        print(f'<!>{self._length} films chargés sur {nb_films_file} films dans le fichier\n')
        
    @property
    def sugg_Aleatoire(self) -> Film:
        if self._length != 0:
            id_random = int(random.randrange(1,self._length,1))
            suggestion_film = self._movie_list[str(id_random)]
            return suggestion_film
        else:
            print('<!!> Base vide !\n')
            pass



    def retirer(self,filename : str,id  = None,titre = None):
        #passage par id
        if titre == None:
            if int(id) <= self._length: #id valide
                film_a_supprimer = self._movie_list[id]
                del self._movie_list[id]
                for id_a_deplacer in range(int(id) + 1,self._length+1):
                    self._movie_list[str(id_a_deplacer - 1)] = self._movie_list[str(id_a_deplacer)]     

                #retirer du fichier
                for attribut in dir(film_a_supprimer):
                    with open(filename, "r+") as f:
                        d = f.readlines()
                        f.seek(0)
                        for i in d:
                            if i != attribut:
                                f.write(i)
                        f.truncate()
            else:
                print(f'<!> Id invalide (taille de la db = {self._length})\n')


        self._length -= 1   


    def afficher(self) -> None:
        print(f'<O> {self._length} élément(s) dans la base <O>\n')
        for id,film in self._movie_list.items():
            print(f'#{id}----------\n {film.info}')


            
        


    def ajouter_Titre(self,titre : str, filename : str, addToFile : bool) -> None:
        movie,found = retrieve_movie_info(titre)
        if found:
            self.ajouter_Film(movie,filename,addToFile = addToFile)
        else:
            print('<!> Not Found!')



    def ajouter_Film(self,film : Film,filename : str, addToFile : bool) -> None:
        self._movie_list[str(self._length + 1)] = film
        self._length += 1
        if addToFile:
            file = open(filename,'a')
            file.write('\n')
            file.write(f'{film.obtenirTitre}\n')
            file.write(f'{film.obtenirDate}\n')
            file.write(f'{film.obtenirOverview}\n')
            file.write(f'{str(film.obtenirVote)}\n')
            file.close()
        pass

    def afficher_informations_Film(self,id : str):
        print(self._movie_list[id].info)


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
