# Toon.py  Class for each Character.  Holds nearly all of the information
# about the in-game player-character.

# imports:

# Class
class Toon():
    """Toon class holds character info for each in-game player-character"""

    # Properties:
    toon_id = 0         # need db to do this
    toon_name = ""
    toon_class = ""     # Could do this with a PlayerClass obj
    toon_level = int
    primary_role = "dps"   # This should be tank/dps/heal/hybrid
    secondary_role = "" # same as above, should be ok as None
    toon_gear = object  # maybe an object to hold the gear info from Bnet
    gear_score = 0      # from bnet int should be good here
    toon_dps = 0        # possibly from Raidbots.com, would be nice but not critical
    raider_io = 0       # score from raider.io

    def __init__(self, toon_name: str, toon_class: str, toon_level: int, \
                 primary_role: str, secondary_role: str,toon_gear: object, \
                gear_score: int, toon_dps: int, raider_io: int ) -> None:
        """Desc TBD"""
        
        self.toon_name = toon_name
        self.toon_class = toon_class
        self.toon_level = toon_level
        self.primary_role = primary_role
        self.secondary_role = secondary_role
        self.toon_gear = toon_gear
        self.gear_score = gear_score
        self.toon_dps =toon_dps
        self.raider_io = raider_io










if __name__ == "__main__":
    pass

