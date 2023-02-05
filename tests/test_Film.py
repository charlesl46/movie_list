import path
import sys
 
# directory reach
directory = path.Path(__file__).abspath()
 
# setting path
sys.path.append(directory.parent.parent)
 
# importing
from src.utils import *
from src.DataBase import DataBase

init()

db = DataBase()
db.afficher()
