from clubs import *
from init_world import *
from event import *

class Match(object):
    """ Match"""

    def __init__(self, local_club, visitor_club):
        self.local = local_club
        self.visitor = visitor_club  

    def run(self):
        """Simulate the game play"""
        self.events = [] 
        new_event = generate_event(self) 
        self.events.append(new_event)
