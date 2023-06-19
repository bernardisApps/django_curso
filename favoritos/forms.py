from django import forms
from .models import Favorito

class FavoritoModelForm(forms.ModelForm):
    class Meta:
        model = Favorito
        fields = '__all__'