from django import forms
from .models import Toon, EventPost

class ToonEntry(forms.ModelForm):
 
    class Meta:
        model = Toon
        fields = "__all__"

class EventEntry(forms.ModelForm):
# Need to get it to set author as User who created it. and redirect to main page
    class Meta:
        model = EventPost
        # fields = "__all__"
        exclude = ["participants"]