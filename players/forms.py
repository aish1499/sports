from django import forms
from .models import Players

class PlayersForm(forms.ModelForm):
class Meta:
        model = Players
        fields = ( 'image', 'user','content')
        exclude = ('',)

        