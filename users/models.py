from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 200, unique=True)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    email = models.EmailField(unique=True, null=False)
    password  = models.CharField(max_length=50, null= False)

    def __str__(self):
        return self.username