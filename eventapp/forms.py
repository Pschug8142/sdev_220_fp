from django import forms
from .models import Toon, EventPost

class ToonEntry(forms.ModelForm):
 
    class Meta:
        model = Toon
        fields = "__all__"

class EventEntry(forms.ModelForm):

    class Meta:
        model = EventPost
        fields = "__all__"