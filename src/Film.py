import urllib.request


class Film:
    """ A class to manipulate films, including their title, date, overview, their poster url and their average note by public"""
    
    
    def __init__(self,title : str,date : str,overview : str,poster_path : str,vote_average : str) -> None:
        """Method to initialize a Film object

        Args:
            title (str): the title
            date (str): the date
            overview (str): the overview
            poster_path (str): the poster path
            vote_average (str): their average note
        """
        self._title = title
        self._date = date
        self._overview = overview
        self._poster_path = poster_path
        self._vote_average = vote_average
        pass


    @classmethod
    def empty(self):
        """Method to init the empty film"""
        return Film('','','','','')


    def set_title(self,title : str) -> None:
        """Method to set the title of a Film

        Args:
            title (str): the title
        """
        self._title = title
    pass


    def set_date(self,date : str) -> None:
        """Method to set the date of a Film

        Args:
            date (str): the date
        """
        self._date = date
    pass


    def set_overview(self,over : str) -> None:
        """Method to set the overview of a Film

        Args:
            over (str): the overview
        """
        self._overview = over
    pass

    def set_vote(self,vote : str) -> None:
        """Method to set the average note of a Film

        Args:
            vote (str): the average note
        """
        self._vote_average = vote
    pass

    @property
    def get_title(self) -> str:
        """Method to get the title of a Film

        Returns:
            str: the title
        """
        return self._title

    

    @property
    def get_date(self) -> str:
        """Method to get the date of a Film

        Returns:
            str: the date
        """
        return self._date

    @property
    def get_vote(self) -> str:
        """Method to get the average note of a Film

        Returns:
            str: the average note
        """
        return self._vote_average

    @property
    def get_overview(self) -> str:
        """Method to get the overview of a Film

        Returns:
            str: the overview
        """
        return self._overview

    @property
    def get_info(self) -> str:
        """Method to get a summary of all the info of the Film

        Returns:
            str: the summary
        """
        return(f'{self.get_title}\n'
        + f'\t Sorti en : {self.get_date} \n'
        + f'\t Aimé à {int(self.get_vote) * 10} %\n'
        + f'\t Résumé : {self.get_overview} ')


    def download_poster(self):
        
        try:
            urllib.request.urlretrieve(f"https://image.tmdb.org/t/p/original/{self.poster_path}",filename=f"posters/{self.title}_poster")
        except ValueError:
            print('<!> URL du poster invalide\n')













