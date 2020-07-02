from django import forms
from .models import LastFMGraph

class LastFMGraphForm(forms.ModelForm):
    class Meta:
        model = LastFMGraph
        fields = ('user1', 'user2',)
        labels = {
            'user1': "User 1",
            'user2': "User 2"
        }

    def __init__(self, *args, **kwargs):
        super(LastFMGraphForm, self).__init__(*args, **kwargs)
        self.fields['user2'].required = False