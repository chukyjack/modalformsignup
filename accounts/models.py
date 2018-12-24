from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.user.username} Profile'
