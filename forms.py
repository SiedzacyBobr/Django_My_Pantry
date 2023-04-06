from django import forms
from .models import Products
from django.db.models import F

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name','unit','quty', 'sefty', 'category']

class QuantityForm(forms.Form):
    def __init__(self, *args, **kwarks):
        super().__init__(*args, **kwarks)
      
        self.fields['number']=forms.IntegerField(
            label='Wprowadź wartość', 
            )
        
class QuantitymaxForm(forms.Form):
    def __init__(self, pk, *args, **kwarks):

        self.maximum = Products.objects.get(id=pk).quty

        super().__init__(*args, **kwarks)

        self.fields['number']=forms.IntegerField(
            label='Wprowadź wartość', 
            min_value=0,
            initial=0,
            max_value=self.maximum,
            )
        





# Badanie zatrudnienia Absolwentów i Absolwentek SDA
# Dziękujemy za poświęcony czas i wypełnienie ankiety. Jeśli chcesz z nami porozmawiać jesteśmy do Twojej dyspozycji pod numerem 729 086 579 lub mailowo doradcakariery@sdacademy.pl