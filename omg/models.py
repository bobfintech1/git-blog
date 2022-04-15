from django.db import models

# Create your models here.

class UserModel(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    country = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    sex = models.BooleanField()
    salary = models.FloatField()


    def __str__(self):
        return str(self.name)