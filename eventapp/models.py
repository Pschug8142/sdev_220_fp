# Create your models here.
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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
    # participants needs to be an array of class Toon's
    # participants = models.ForeignObject(Toon) not sure how to do this


    def publish(self):
        self.event_date = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.title} {self.event_date}'

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # toon = models.ForeignKey(Toon, null=False, on_delete=models.CASCADE) Not possible would make many to many

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

    player_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # the human player
    name = models.CharField(max_length=12)
    realm = models.CharField(max_length=30)
    realm_region = models.CharField(max_length=10, choices=regions, default="americas")
    level = models.IntegerField(default=70)
    primary_role = models.CharField(max_length=10, choices=roles, default="damage")
    secondary_role = models.CharField(max_length=10, choices=roles, null=True)
    gear_score = models.IntegerField(default=0)
    # ToDo: add items for gear, io score, and DPS

    def __str__(self) -> str:
        return f'{self.name} {self.player_name} {self.primary_role} {self.gear_score}'
    