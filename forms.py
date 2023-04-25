from django import forms
from .models import Products, Kategoria
from django.db.models import F
# from django.conf import settings
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, get_user_model, get_user
# from django.contrib.auth import update_session_auth_hash


# user_set = settings.AUTH_USER_MODEL
# print(f" to jest zalogowany użytkownik ====================================1==========================================> {user_set}")


# user_model = get_user
# print(f"to jest kolejna proba zbobyćia id użytkownkika ========================2=====================================> {user_model}")


# user_login = User
# print(f" To są wybrane kategorie użytkownika ===================================4===================================> {user_login}")

# user = 4
# userkategory= Kategoria.objects.filter(user_id=user)
# print(f" To są wybrane kategorie użytkownika ===================================3===================================> {userkategory}")

# for i in userkategory:
#     print(f"Teścik i: =======5=========> {i} <===============")




# MY_KATEGORY = (('1', "zaścianą"),("2","podschodami",))

class ProductsForm(forms.ModelForm):

    name = forms.CharField(label="Nazwa produktu:", initial="np. makaron świderki",)
    unit = forms.CharField(label=" Jednostka miary:", initial="np. 1kg",)
    quty = forms.IntegerField(label="Ilość wprowadzana:", min_value=0,)
    sefty = forms.IntegerField(label="Żelazny zapas:", min_value=0,)
    # category = forms.ChoiceField(label="Kategoria:", choices=Kategoria)
    
    class Meta:
        model = Products
        fields = '__all__'
        exclude = ['user']

class KategoriaForm(forms.ModelForm):

    cate = forms.CharField(label="Nazwa kategorii", help_text="np. sypkie",)

    class Meta:
        model = Kategoria
        fields = ['cate']
        

        

# Badanie zatrudnienia Absolwentów i Absolwentek SDA
# Dziękujemy za poświęcony czas i wypełnienie ankiety. Jeśli chcesz z nami porozmawiać jesteśmy do Twojej dyspozycji pod numerem 729 086 579 lub mailowo doradcakariery@sdacademy.pl