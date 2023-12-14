from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import EventPost, Toon, Player

class PlayerInLine(admin.StackedInline):
    model = Player
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = [PlayerInLine]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(EventPost)
admin.site.register(Toon)
admin.site.register(Player)