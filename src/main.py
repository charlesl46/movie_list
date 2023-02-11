"""Main module of the project"""

from WatchList import WatchList
import click


@click.command()
def main():
    wl = WatchList()
    wl.menu()
    

if __name__ == "__main__":
    main()


