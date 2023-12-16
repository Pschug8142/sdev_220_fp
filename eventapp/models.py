# Create your models here.
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from api_functions import raiderIo_request, create_access_token, character_access_request, item_access_request, profile_access_request



class Player(models.Model):
    """The Player class was created to serve as an intermediary between the User and the Toon class.
    Currently, it is unused, as the User seems to work ok for the purposes of the app. It does get
    populated with User info on a one to one basis.
    """
    name = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name}'


class Toon(models.Model):
    """The Toon class holds everything on the site about each WoW character. And interfaces with 
    API calls to battle.net and raider.io (a website that tracks character stats).  The player_name
    property references the User.  A user may have multiple Characters (Toon) on the site.  
    Toon creation is done via a link on the site using the forms.ModelForm creator"""
    
    # regions, roles, and wow_classes are tuples for choice menus in the ModelForm creator
    regions = (
        ("americas", "Americas"),
        ("europe", "Europe"),
        ("korea", "Korea"),
        ("taiwan", "Taiwan"),
    )
    roles = (
        ("tank", "Tank"),
        ("heal", "Heal"),
        ("damage", "Damage"),
        ("hybrid", "Hybrid"),
        ("none", "None"),
    )
    wow_classes = (
        ("death_knight", "Death Knight"),
        ("demon_hunter", "Demon Hunter"),
        ("druid", "Druid"),
        ("evoker", "Evoker"),
        ("hunter", "Hunter"),
        ("mage", "Mage"),
        ("monk", "Monk"),
        ("paladin", "Paladin"),
        ("priest", "Priest"),
        ("rogue", "Rogue"),
        ("shaman", "Shaman"),
        ("warlock", "Warlock"),
        ("warrior", "Warrior"),
    )

    player_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # the human player
    name = models.CharField(max_length=12)  # Character name
    realm = models.CharField(max_length=30) # WoW realm character is on
    realm_region = models.CharField(max_length=10, choices=regions, default="americas") # realm region from regions above
    level = models.IntegerField(default=70) # max level currently 70
    tclass = models.CharField(max_length=30, choices=wow_classes, default="death_knight") # Character class
    primary_role = models.CharField(max_length=10, choices=roles, default="damage") # from roles above
    secondary_role = models.CharField(max_length=10, choices=roles, null=True)      # ""   ""
    gear_score = models.IntegerField(default=0) # should be pulled from raider.io api (not implemented) currently manually entered
    # ToDo: add items for gear, io score, and DPS
    # 
 
    def get_raiderio(self):
        """Fetch a json from the raider.io website and return it for further processing. This calls
        a function from the api_handler module."""
        print("get_raiderio called")    # debug
        try:
            io_json = raiderIo_request(self.name, self.realm)
            print(io_json)
            # return io_json  #not currently implemented the json is printed to console above and works as intended.
        except:
            print(f"Something bad happened in get_raiderio")

    def get_api_gear(self):
        """Fetch a json from the battle.net website and return it for further processing. This calls
        a function from the api_handler module."""
        # Not currently implemented
        print("get_api_gear called")    # debug
        try:
            pass
        except:
            print(f"Something bad happened in get_api_gear")

    def __str__(self) -> str:
        return f'{self.name} {self.player_name} {self.primary_role} {self.gear_score}'


class EventPost(models.Model):
    """Class for the Events themselves.  Events are created with the ModelForm form which auto creates the form
    author should be the logged in user, participants are filled in as users click to sign up.  Other
    fields are entered in the form creating the event."""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    event_type = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    event_date = models.DateTimeField(blank=True, null=True)
    min_participants = models.IntegerField(default=0, null=True)
    max_participants = models.IntegerField(default=0, null=True)
    participants = models.ManyToManyField(Toon)   
    # participants = models.CharField(max_length=255, default="foo")

    
    def get_participants(self):
        """Should return a list of participants for the roster."""
        # currently is not getting filled and returns None
        print(self.participants)
        return self.participants.name

    def publish(self):
        self.event_date = timezone.now()
        self.save()
    
    def add_signup(self, user):
        """Method to add a user to the event roster"""
        # not working
        print(f"add {user}")
        EventSignUp.objects.create(user = user, event = self)
        self.participants.add(user)
        
    def del_signup(self, user):
        """Method to remove a user from the event roster"""
        # not working
        registration = EventSignUp.objects.get(user = user, event = self)
        registration.delete()
    
    def get_signups(self):
        # not working
        return EventSignUp.objects.filter(event = self)

    def __str__(self):
        return f'{self.title}'


class EventSignUp(models.Model):
    """A class to allow participants to sign up for events  Not currently working"""
    event = models.ForeignKey(EventPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    toon = models.ForeignKey(Toon, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user.username}'
    
    class Meta:
        verbose_name = 'Attendee'
        verbose_name_plural = 'Attendees'
        unique_together = ('event', 'user')

    def save(self, *args, **kwargs):
        super(EventSignUp, self).save(*args, **kwargs)
