from clubs import *
from person import *

def generate_clubs():
    """ initiate clubs"""
    clubs = []
    clubs.append( Club("River Plate") )
    clubs.append( Club("Boca Juniors") )
   
    return clubs 

def generate_fplayers(clubs):
    """ Generate players and assign them to clubs"""
    fplayer = Person("J. Riquelme") 
    clubs[1].fplayers.append(fplayer)

    fplayer = Person("E. Francescoli")
    clubs[0].fplayers.append(fplayer)
    
