class Event:
    pass

class Goal_Event(Event):
    """ Goal """
    def __init__(self, match, club, player):
        self.club = club
        self.match = match
        self.player = player

def generate_event(match):
    """ Generate an event in a match"""
    new_event = Goal_Event(match, match.local, match.local.fplayers[0]) 
    return new_event
