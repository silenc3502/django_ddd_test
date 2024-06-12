from django.db import models
from django.utils import timezone
from .account_login_type import AccountLoginType
from .account_role_type import AccountRoleType


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    login_type = models.ForeignKey(AccountLoginType, on_delete=models.CASCADE)
    role_type = models.ForeignKey(AccountRoleType, on_delete=models.CASCADE)

    def __str__(self):
        return f"Account {self.id}"

    class Meta:
        db_table = 'account'
        app_label = 'account'
