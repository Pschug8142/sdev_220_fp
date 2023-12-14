from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ToonEntry(forms.Form):
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
    )

    toon_name = forms.CharField(label='Character Name:', max_length=18, required=True, help_text='')
    realm_name = forms.CharField(label='Realm:', max_length=30, required=True, help_text='')
    region = forms.ChoiceField(label='Region:', required=True, label='', choices=regions)
    toon_role = forms.ChoiceField(label='Primary Role:', required=True, label='', choices=roles)
    toon_role = forms.ChoiceField(label='Primary Role:', required=True, label='', choices=roles)
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'toon_name', 'realm_name', 'region', 'toon_role']