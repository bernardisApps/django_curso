from django import forms
from .models import Favorito

class FavoritoModelForm(forms.ModelForm):
    class Meta:
        model = Favorito
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'url' : forms.URLInput(attrs={'class' : 'form-control'}),
        }