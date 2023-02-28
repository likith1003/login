from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(("Name of the user"), max_length=50)
    username=models.CharField(("Username of the user"), max_length=50)
    password=models.CharField(("Password of the user"), max_length=50)
    def __str__(self):
        return self.name