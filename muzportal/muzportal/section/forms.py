import datetime

from django import forms


class ArtistForm(forms.Form):
    name = forms.CharField(label='Название исполнителя', min_length=2, max_length=128, required=True)
    start_year = forms.IntegerField(label='Год основания', min_value=1900, max_value=2022, required=True,
                                    initial=datetime.datetime.today().year)
