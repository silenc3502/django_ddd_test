from django.db import models

from .account import Account

class Profile(models.Model):
    nickname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname

    class Meta:
        db_table = 'profile'
        app_label = 'account'
