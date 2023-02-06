"""A module to manage a DataBase class"""

from tmdbv3api import Movie
from Film import Film
from tqdm import tqdm
import random

class DataBase:
    """A class designed to manage Film Objects"""
    def __init__(self, filename : str) -> None:
        self.filename = filename
        movie_list = {}
        self._movie_list = movie_list
        self._length = 0
        pass

    
    def is_empty(self) -> bool:
        """Method to know if the db is empty

        Returns:
            bool: is the db empty ?
        """
        return self._length == 0

    def empty(self) -> None:
        """A method to empty the db
        """

        file = open(self.filename, 'w').close()
        self._movie_list.clear()
        self._length = 0
        pass

    def load_movie_info(self):
        """A method to load movies into the db from a file
        """
        file = open(self.filename,'r')
        in_loop = False
        print('<#> Loading ... <#>\n')
        nb_films_file = 0
        for line in tqdm(file):

            if in_loop:
                count = count - 1
                if count == 3:
                    film.set_title(line)
                elif count == 2:
                    film.set_date(line)
                elif count == 1:
                    film.set_overview(line)
                elif count == 0:
                    film.set_vote(line)
                    self.add_film(film = film)

                    in_loop = False
            else:
                nb_films_file += 1
                film = Film.empty()
                in_loop = True
                count = 4
        print(f'<!>{self._length} films loaded for {nb_films_file} films in {self.filename} file\n')
        pass
        
    @property
    def random_suggestion(self) -> Film:
        """A method to give a random suggestion in the db

        Returns:
            Film: the random suggestion
        """
        print(f'length = {self._length}')
        if self._length == 1:
            return self._movie_list['1']
        elif not self.is_empty():
            id_random = int(random.randrange(1,self._length,1))
            print(f'numero {id_random}')
            suggestion_film = self._movie_list[str(id_random)]
            return suggestion_film
        else:
            print('<!!> Database empty !\n')
            return Film.empty()



    def remove(self,id  = None,title = None):
        """A method to remove a film from the db, either from its id or from its title

        Args:
            id (_type_, optional): the id of the film to remove. Defaults to None.
            title (_type_, optional): the title of the film to remove. Defaults to None.
        """
        
        if title == None:
            if int(id) <= self._length:
                film_to_remove = self._movie_list[id]
                del self._movie_list[id]
                for id_to_move in range(int(id) + 1,self._length+1):
                    self._movie_list[str(id_to_move - 1)] = self._movie_list[str(id_to_move)]     

                for attribute in dir(film_to_remove):
                    with open(self.filename, "r+") as f:
                        d = f.readlines()
                        f.seek(0)
                        for i in d:
                            if i != attribute:
                                f.write(i)
                        f.truncate()
            else:
                print(f'<!> Error : invalid id (db size = {self._length} films) <!>\n')


        self._length -= 1 
        pass


    def show(self) -> None:
        """A function to show the current state of the db with all the films stored in it"""
        print(f'<#> {self._length} element(s) in the database <#>\n')
        for id,film in self._movie_list.items():
            print(f'#{id}----------\n {film.get_info}')
            print('\n\n')
        pass



            
        


    def add_film(self,title : str = None, film : Film = None) -> None:
        """A method to add a film to the db, either by title or by Film object directly 

        Args:
            title (str, optional): the title to add. Defaults to None.
            film (Film, optional): the Film to add. Defaults to None.
        """
        

        if film == None:
            film,found = self.retrieve_film_info(title)
            if not found:
                print('<!> Not Found! <!>')
            file = open(self.filename,'a')
            file.write('\n')
            file.write(f'{film.get_title}\n')
            file.write(f'{film.get_date}\n')
            file.write(f'{film.get_overview}\n')
            file.write(f'{str(film.get_vote)}\n')
            file.close()

        self._movie_list[str(self._length + 1)] = film
        self._length += 1

        





    def show_info_film(self,id : str) -> None:
        """A method to show info about a film

        Args:
            id (str): the id of the film to give info of
        """
        if int(id) <= self._length:
            print(self._movie_list[id].get_info)
        else:
            print(f'<!> Error : invalid id (db size = {self._length} films) <!>\n')


    def retrieve_film_info(self,title : str):
        """A method to retrieve info on a film using tmdb api

        Args:
            title (str): the title of the film

        Returns:
            Film: the film found
            bool: if the film was found
        """
        movie = Movie()
        search = movie.search(title)
        if len(search) != 0:
            title = search[0].title
            date = search[0].release_date
            overview = search[0].overview
            poster_path = search[0].poster_path
            vote_average = round(search[0].vote_average)
            film = Film(title,date,overview,poster_path,vote_average)
            return film,True
        else:
            return Film.empty(),False
