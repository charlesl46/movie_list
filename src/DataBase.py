from Film import Film
import utils as ut

class DataBase:
    def __init__(self) -> None:
        movie_list = {}
        self._movie_list = movie_list
        self._length = 0
        pass

    
    def vider(self) -> None:
        self.movie_list.clear
        self.length = 0

    def load_movie_info(self,filename : str):
        file = open(filename,'r')
        inLoop = False
        for line in file:
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
                    self.ajouter_Film(film)
                    inLoop = False
            else:
                film = Film.empty()
                inLoop = True
                count = 4
    
    def afficher(self) -> None:
        print(f'<O> {self._length} élément(s) dans la base <O>\n')
        for id,film in self._movie_list.items():
            print(f'#{id}----------\n {film.info}')


            
        


    def ajouter_Titre(self,titre : str) -> None:
        movie,found = ut.retrieve_movie_info(titre)
        if found:
            self.ajouter_Film(movie)
        else:
            print('<!> Not Found!')



    def ajouter_Film(self,film : Film) -> None:
        self._movie_list[str(self._length + 1)] = film
        self._length += 1
        pass

    def afficher_informations_Film(self,id : str):
        print(self._movie_list[id].info)


