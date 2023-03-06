from django import forms
from .models import Products

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name','unit','quty', 'sefty', 'category']


#======================================================================

class QuantityForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs): #
        max_value =12
        super().__init__(*args, **kwargs)
        self.fields['quty'].widget.attrs.update({'min':0, 'max': max_value,})
        self.fields['quty'].label='Wprowadź wartość'
               
        
    class Meta:
        model = Products
        fields = ['quty']

#========================================================================




class LiczbaForm(forms.Form):
    liczba = forms.DecimalField(label='', min_value=0, initial=0)

