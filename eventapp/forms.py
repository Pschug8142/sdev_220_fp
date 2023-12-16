from django import forms
from .models import Toon, EventPost

class ToonEntry(forms.ModelForm):
    """Class for forms.ModelForm character entry form."""
 
    class Meta:
        model = Toon
        fields = "__all__"

class EventEntry(forms.ModelForm):
    """Class for forms.ModelForm auto form creation for the events"""
    # Need to get it to set author as User who created it. and redirect to main page
    class Meta:
        model = EventPost
        # fields = "__all__"
        exclude = ["participants"]  # participants should be filled later by the users