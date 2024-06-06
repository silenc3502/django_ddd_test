from django.db import models
from django.utils import timezone
from .account_login_type import AccountLoginType
from .account_role_type import AccountRoleType


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    create_date = models.DateTimeField(auto_now_add=True)
    last_login_date = models.DateTimeField(default=timezone.now)
    login_type = models.OneToOneField(AccountLoginType, on_delete=models.CASCADE)
    role_type = models.OneToOneField(AccountRoleType, on_delete=models.CASCADE)

    def __str__(self):
        return f"Account {self.id}"

    class Meta:
        app_label = 'account'
