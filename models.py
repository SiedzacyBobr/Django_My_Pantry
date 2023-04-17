from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



class Kategoria(models.Model):
    cate = models.CharField(null=True, max_length=100)

    def __str__(self) -> str:
        return f" {self.cate}"


class Products(models.Model):
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=10)
    quty = models.IntegerField()
    sefty = models.IntegerField()
    category = models.ForeignKey(Kategoria, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   
    def __str__(self) -> str:
        return f" {self.name} "



# Create your models here.

# zawierdzenie bazy danych ==> py manage.py makemigrations
# wysłanie bazy danych ==> py manage.py migrate 