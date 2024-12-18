from django import forms
from .models import Client,Produit

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'