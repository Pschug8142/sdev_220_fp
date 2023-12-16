# Create your models here.
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from api_functions import raiderIo_request
# from .models import EventSignUp


class Player(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name}'


class Toon(models.Model):
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
    name = models.CharField(max_length=12)
    realm = models.CharField(max_length=30)
    realm_region = models.CharField(max_length=10, choices=regions, default="americas")
    level = models.IntegerField(default=70)
    tclass = models.CharField(max_length=30, choices=wow_classes, default="death_knight")
    primary_role = models.CharField(max_length=10, choices=roles, default="damage")
    secondary_role = models.CharField(max_length=10, choices=roles, null=True)
    gear_score = models.IntegerField(default=0)
    # ToDo: add items for gear, io score, and DPS

    
    def get_api_gear(self):
        print("get_api_gear called")
        try:
            io_json = raiderIo_request(self.name, self.realm)
            print(io_json)
        except:
            print(f"Something bad happened")

    def __str__(self) -> str:
        return f'{self.name} {self.player_name} {self.primary_role} {self.gear_score}'

# Needs participants/toon/role.  
class EventPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    event_type = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    event_date = models.DateTimeField(blank=True, null=True)
    min_participants = models.IntegerField(default=0, null=True)
    max_participants = models.IntegerField(default=0, null=True)
    participants = models.ManyToManyField(Toon)
    
    
    def get_participants(self):
        print(self.participants)
        return self.participants.name

    def publish(self):
        self.event_date = timezone.now()
        self.save()
    
    def add_signup(self, user):
        print(f"add {user}")
        EventSignUp.objects.create(user = user, event = self)
        self.participants.add(user)
        
    def del_signup(self, user):
        registration = EventSignUp.objects.get(user = user, event = self)
        registration.delete()
    
    def get_signups(self):
        return EventSignUp.objects.filter(event = self)

    def __str__(self):
        return f'{self.title}'


class EventSignUp(models.Model):
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














# # Create your models here.
# from django.conf import settings
# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone
# # from .models import EventSignUp


# class Player(models.Model):
#     name = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self) -> str:
#         return f'{self.name}'


# # Needs participants/toon/role.  
# class EventPost(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     event_type = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     event_date = models.DateTimeField(blank=True, null=True)
#     min_participants = models.IntegerField(default=0, null=True)
#     max_participants = models.IntegerField(default=0, null=True)
#     participants = models.ManyToManyField(Player)
    
#     @property
#     def get_participants(self):
#         print(self.participants)
#         return self.participants.name

#     def publish(self):
#         self.event_date = timezone.now()
#         self.save()
    
#     def add_signup(self, user):
#         print(f"add {user}")
#         #EventSignUp.objects.create(user = user, event = self)
#         self.participants.add(user)
        
#     def del_signup(self, user):
#         registration = EventSignUp.objects.get(user = user, event = self)
#         registration.delete()
    
#     def get_signups(self):
#         return EventSignUp.objects.filter(event = self)

#     def __str__(self):
#         return f'{self.title}'



# class Toon(models.Model):
#     regions = (
#         ("americas", "Americas"),
#         ("europe", "Europe"),
#         ("korea", "Korea"),
#         ("taiwan", "Taiwan"),
#     )
#     roles = (
#         ("tank", "Tank"),
#         ("heal", "Heal"),
#         ("damage", "Damage"),
#         ("hybrid", "Hybrid"),
#         ("none", "None"),
#     )
#     wow_classes = (
#         ("death_knight", "Death Knight"),
#         ("demon_hunter", "Demon Hunter"),
#         ("druid", "Druid"),
#         ("evoker", "Evoker"),
#         ("hunter", "Hunter"),
#         ("mage", "Mage"),
#         ("monk", "Monk"),
#         ("paladin", "Paladin"),
#         ("priest", "Priest"),
#         ("rogue", "Rogue"),
#         ("shaman", "Shaman"),
#         ("warlock", "Warlock"),
#         ("warrior", "Warrior"),
#     )

#     player_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # the human player
#     name = models.CharField(max_length=12)
#     realm = models.CharField(max_length=30)
#     realm_region = models.CharField(max_length=10, choices=regions, default="americas")
#     level = models.IntegerField(default=70)
#     tclass = models.CharField(max_length=30, choices=wow_classes, default="death_knight")
#     primary_role = models.CharField(max_length=10, choices=roles, default="damage")
#     secondary_role = models.CharField(max_length=10, choices=roles, null=True)
#     gear_score = models.IntegerField(default=0)
#     # ToDo: add items for gear, io score, and DPS

#     def get_api_gear(self):
#         try:
#             # gear_dict = {}
#             # gear_dict = skugs_api_call(self.name, self.realm_region, self.realm)
#             # return gear_dict
#             pass
#         except:
#             pass

#     def __str__(self) -> str:
#         return f'{self.name} {self.player_name} {self.primary_role} {self.gear_score}'
    

# class EventSignUp(models.Model):
#     event = models.ForeignKey(EventPost, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     toon = models.ForeignKey(Toon, on_delete=models.CASCADE)

#     def __str__(self) -> str:
#         return f'{self.user.username}'
    
#     class Meta:
#         verbose_name = 'Attendee'
#         verbose_name_plural = 'Attendees'
#         unique_together = ('event', 'user')

#     def save(self, *args, **kwargs):
#         super(EventSignUp, self).save(*args, **kwargs)
