from django import forms
from .models import Products, Kategoria
from django.db.models import F
from django.utils.translation import gettext_lazy as _

class ProductsForm(forms.ModelForm):

    name = forms.CharField(label="Nazwa produktu:", )
    unit = forms.CharField(label=" Jednostka miary:",)
    quty = forms.IntegerField(label="Ilość wprowadzana:", min_value=0, )
    sefty = forms.IntegerField(label="Żelazny zapas:", min_value=0,)
    
    class Meta:
        model = Products
        fields = '__all__'
        exclude = ['user']
        labels = {"category":_("Kategoria")}
    
    def __init__ (self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['category'].choices = Kategoria.objects.filter(user_id=user).values_list('id', 'cate')


class KategoriaForm(forms.ModelForm):

    cate = forms.CharField(label="Nazwa kategorii",)

    class Meta:
        model = Kategoria
        fields = ['cate']
        

        

# Badanie zatrudnienia Absolwentów i Absolwentek SDA
# Dziękujemy za poświęcony czas i wypełnienie ankiety. Jeśli chcesz z nami porozmawiać jesteśmy do Twojej dyspozycji pod numerem 729 086 579 lub mailowo doradcakariery@sdacademy.pl