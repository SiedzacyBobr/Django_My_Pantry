from django.db import models

class Kategoria(models.Model):
    cate = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f" {self.cate}"

class Products(models.Model):
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=10)
    quty = models.IntegerField()
    sefty = models.IntegerField()
    category = models.ForeignKey(Kategoria, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f" {self.name} "

# Create your models here.
