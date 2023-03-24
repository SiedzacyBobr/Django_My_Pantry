from django import forms
from .models import Products

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name','unit','quty', 'sefty', 'category']


#======================================================================

class QuantityForm(forms.ModelForm):
    
    def __init__(self, max_value, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['quty'].widget.attrs.update({'min':0, 'max': max_value})
        self.fields['quty'].label = 'Wprowadź wartość'
        print("udało się 19 forms")
               
        
    class Meta:
        model = Products
        fields = ['quty']

#========================================================================


class LiczbaForm(forms.Form):
    liczba = forms.DecimalField(label='', min_value=0, initial=0)

