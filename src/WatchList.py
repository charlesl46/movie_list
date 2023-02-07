"""A module to manage a Watchlist class"""

from DataBase import DataBase
from tmdbv3api import TMDb, Movie
from tqdm import tqdm
import os


class WatchList:
    """A Class to manage a Movies WatchList from a Database located in file
    A WatchList object is made of a description and a DataBase object"""

    def __init__(self) -> None:
        """Method to init a Watchlist"""

        print('<#> From which file import the database ? (.mwl.txt files): <#>\n')
        print('\tdata folder :\n')
        for file in os.listdir('../data'):
            if file.endswith('.mwl.txt'):
                size = os.stat(f'../data/{file}').st_size / (1024**2)
                print(f'\t- {file} | {round(size,2)} Mo\n')

        input_ok = False
        while not input_ok:
                base_name = input()
                if base_name in os.listdir('../data'):
                    input_ok = True
                else:
                    print('<!> Error : file name not correct ! Please, try again <!>\n')
        

        self.filename = f'../data/{base_name}'
        self.db = DataBase(self.filename)
        self.db.load_movie_info()

        print('<#> Do you want to give a name to this Watchlist (y/n)? <#>\n')
        enter_a_name = bool(input() == 'y')
        if enter_a_name:
            print('<#> What\'s the name ? <#>\n')
            self.name = str(input())
        else:
            self.name = self.filename.rstrip('.mwl.txt').lstrip('../data/')

        #connecting to tmdb api
        print('<#> Loading API... <#>')
        tmdb = TMDb()
        tmdb.api_key = 'a5beed50b62bc4886b8da6bb2b823fa3'
        tmdb.language = 'fr'
        tmdb.debug = True

        pass

    def menu(self) -> None:
        """Method to display main menu of the WatchList"""
        finished = False


        print(f'<#> Welcome to {self.name} movie database <#>\n')
        while not finished:
            print('<#> What do you want to do ? <#>\n')
            print('\t - <1> Show current watchlist\n')
            print('\t - <2> Show a film\'s info\n')
            print('\t - <3> Add a film\n')
            print('\t - <4> Get a random suggestion from the watchlist\n')
            print('\t - <5> Empty active watchlist\n')
            print('\t - <6> Remove a film\n')
            print('\t - <7> To close this program, hit #\n')

            choice = input()
            if choice == '#':
                finished = True
            elif choice == '1':
                self.db.show()
            elif choice == '2':
                print('<#> Which film (id)?\n')
                id = input()
                self.db.show_info_film(str(id))
            elif choice == '3':
                print('<#> Which film (title)?\n')
                titre = input()
                self.db.add_film(title = titre)
            elif choice == '4':
                print('<#> Here\'s a suggestion : \n')
                print(self.db.random_suggestion.get_info)
            elif choice == '5':
                self.db.empty()
                print(f'<#> {self.name} movie database emptied... <#>')
            elif choice == '6':
                print('<#> Remove by id or by title (id/title) ?\n')
                c = input()
                if c == 'id':
                    print('Which id ?\n')
                    id = str(input())
                    self.db.remove(id = id)
                else:
                    print('Which title ?\n')
                    title = str(input())
                    self.db.remove(title = title)

        print('</o\> Thank\'s for using! </o\>')

    
