from django import forms
from .models import Products, Kategoria
from django.db.models import F

class ProductsForm(forms.ModelForm):

    name = forms.CharField(label="Nazwa produktu:", initial="np. makaron świderki",)
    unit = forms.CharField(label=" Jednostka miary:", initial="np. 1kg",)
    quty = forms.IntegerField(label="Ilość wprowadzana:", min_value=0, max_value=12, )
    sefty = forms.IntegerField(label="Żelazny zapas", min_value=0, max_value=12, )
    
    class Meta:
        model = Products
        fields = '__all__'
        exclude = ['user']
        

        

# Badanie zatrudnienia Absolwentów i Absolwentek SDA
# Dziękujemy za poświęcony czas i wypełnienie ankiety. Jeśli chcesz z nami porozmawiać jesteśmy do Twojej dyspozycji pod numerem 729 086 579 lub mailowo doradcakariery@sdacademy.pl