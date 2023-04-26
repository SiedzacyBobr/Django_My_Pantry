from django import forms
from .models import Products, Kategoria
from django.db.models import F

class ProductsForm(forms.ModelForm):

    name = forms.CharField(label="Nazwa produktu:", help_text=" ",)
    unit = forms.CharField(label=" Jednostka miary:", help_text="  np. 400g",)
    quty = forms.IntegerField(label="Ilość wprowadzana:", min_value=0, help_text="  Ile jest w chwili jej dodawania",)
    sefty = forms.IntegerField(label="Żelazny zapas:", min_value=0, help_text="  Minimalna ilość jaka zawsze musi być",)
    
    class Meta:
        model = Products
        fields = '__all__'
        exclude = ['user']
    
    def __init__ (self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['category'].choices = Kategoria.objects.filter(user_id=user).values_list('id', 'cate')


class KategoriaForm(forms.ModelForm):

    cate = forms.CharField(label="Nazwa kategorii", help_text="  np. lodówka",)

    class Meta:
        model = Kategoria
        fields = ['cate']
        

        

# Badanie zatrudnienia Absolwentów i Absolwentek SDA
# Dziękujemy za poświęcony czas i wypełnienie ankiety. Jeśli chcesz z nami porozmawiać jesteśmy do Twojej dyspozycji pod numerem 729 086 579 lub mailowo doradcakariery@sdacademy.pl