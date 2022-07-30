from django.db import models

class Familia(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    date = models.DateField(auto_now_add=True,null=True, blank= True)
    email = models.EmailField()