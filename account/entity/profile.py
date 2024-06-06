from django.db import models
from .account_login_type import AccountLoginType

class Profile(models.Model):
    nickname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    profile_image_name = models.CharField(max_length=100)
    account = models.OneToOneField(AccountLoginType, on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname

    class Meta:
        app_label = 'account'
