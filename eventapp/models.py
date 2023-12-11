# Create your models here.
from django.conf import settings
from django.db import models
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

class Toon(models.Model):
    player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # the human player
    name = models.CharField(max_length=12)
    realm = models.CharField(max_length=200)
    level = models.IntegerField(default=0)
    primary_role = models.CharField(max_length=200, default="dps")
    secondary_role = models.CharField(max_length=200, null=True)
    gear_score = models.IntegerField(default=0)
    # ToDo: add items for gear, io score, and DPS

    def __str__(self) -> str:
        return f'{self.name} {self.player} {self.primary_role} {self.gear_score}'