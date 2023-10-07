from django import forms
from .models import Movie

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name','desc','year','img']

class AddMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'desc', 'year', 'img']
