from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(default="")
    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=40,default="")
    place = Place
    isKing= models.BooleanField()
    isDead=models.BooleanField(initial=True)
    def __str__(self):
        return self.nombre

class Stat(models.Model):
    name = models.CharField(max_length=40, default="")
    description = models.CharField(max_length=200,default="")
    def __str__(self):
        return self.name

class Rule(models.Model):
    name= models.CharField(max_length=40,default="Capa")
    description = models.CharField(max_length=200,default="")
    def __str__(self):
        return self.name