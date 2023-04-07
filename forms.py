from django import forms
from .models import Products
from django.db.models import F
from django.utils.translation import gettext_lazy as _

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name','unit','quty', 'sefty', 'category']
        labels = {
            'name':_('Nazwa produktu:_____'),
            'unit':_('Jednostka miary:_____'),
            'quty':_('Wprowadzana ilość:__'),
            'sefty':_('Żelazny zapas:________'),
            'category':_('Kategoria:____________'),
        }
        placeholder= {
            "name": _("Some useful help text."),
            }

        

# Badanie zatrudnienia Absolwentów i Absolwentek SDA
# Dziękujemy za poświęcony czas i wypełnienie ankiety. Jeśli chcesz z nami porozmawiać jesteśmy do Twojej dyspozycji pod numerem 729 086 579 lub mailowo doradcakariery@sdacademy.pl