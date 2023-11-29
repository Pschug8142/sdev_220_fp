import datetime     # clean up imports
import player

class Event():
    """ Event class Basic class for storing data for WoW events"""

    # Properties:
    evid  = 0           # database set?
    event_name = ""
    event_date = datetime.datetime.now()
    event_location = ""
    min_participants = 0
    max_participants = 0
    participants = []

    def __init__(self, event_name: str, event_date: datetime, \
                 event_location: str, min_participants: int, max_participants: \
                 int, participants: list) -> None:
        
        self.evid = 0 # figure out how to have db set
        self.event_name =  event_name
        self.event_date = event_date
        self.event_location = event_location
        self.min_participants = min_participants
        self.max_participants = max_participants
        self.participants = participants    # should be a list (maybe dict) of 
                                            # players/toon objects?

        # Do we need setters and gitters?

    def event_roster(self):
        """ Return a list of current event participants """
        return self.participants
        pass

