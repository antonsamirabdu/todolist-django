from django.forms import ModelForm
from .models import Movies


class MovieForm(ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'
