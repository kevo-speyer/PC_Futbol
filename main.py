from init_world import *
from match import *
from clubs import *
from person import *

# Initiate World ( clubs, persons, etc
clubs = generate_clubs()
generate_fplayers(clubs)

test_match = Match(clubs[0], clubs[1])

test_match.run()


