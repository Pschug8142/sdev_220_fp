import datetime     # clean up import

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
        pass


