from django.db import models

# Create your models here.

# Actually i don't need this model bcs theres one already created 
# auth_user
class User(models.Model):
    username = models.CharField(max_length = 30, unique=True)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(unique=True, null=False)
    password  = models.CharField(max_length=30, null= False)

    def __str__(self):
        return self.username