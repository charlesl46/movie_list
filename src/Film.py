import urllib.request


class Film:
    """ Une classe pour manipuler les films, contenant leur titre, leur résumé, l'url de leur poster et la note moyenne"""
    
    
    def __init__(self,title : str,date : str,overview : str,poster_path : str,vote_average : str) -> None:
        """Le constructeur de la classe Film"""
        self._title = title
        #self.genres = genres
        self._date = date
        #self.origin = origin
        self._overview = overview
        self._poster_path = poster_path
        self._vote_average = vote_average
        pass


    @classmethod
    def empty(self):
        """Le constructeur du film vide"""
        return Film('','','','','')


    def definirTitre(self,title : str) -> None:
        self._title = title
    pass


    def definirDate(self,date : str) -> None:
        self._date = date
    pass


    def definirOverview(self,over : str) -> None:
        self._overview = over
    pass

    def definirVote(self,vote : str) -> None:
        self._vote_average = vote
    pass

    @property
    def obtenirTitre(self) -> str:
        return self._title

    

    @property
    def obtenirDate(self) -> str:
        return self._date

    @property
    def obtenirVote(self) -> str:
        return self._vote_average

    @property
    def obtenirOverview(self) -> str:
        return self._overview

    @property
    def info(self) -> str:
        return(f'<#> {self.obtenirTitre} <#>\n'
        + f'\t<> Sorti en : {self.obtenirDate} \n'
        + f'\t<> Aimé à {int(self.obtenirVote) * 10} %\n'
        + f'\t<> Résumé : {self.obtenirOverview} ')


    def download_poster(self):
        try:
            urllib.request.urlretrieve(f"https://image.tmdb.org/t/p/original/{self.poster_path}",filename=f"posters/{self.title}_poster")
        except ValueError:
            print('<!> URL du poster invalide\n')













