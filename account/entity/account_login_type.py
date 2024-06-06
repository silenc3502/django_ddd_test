from django.db import models

class AccountLoginType(models.Model):
    class LoginType(models.TextChoices):
        KAKAO = 'KAKAO', 'Kakao'

    login_type = models.CharField(max_length=10, choices=LoginType.choices)

    def __str__(self):
        return self.login_type

    class Meta:
        app_label = 'account'
