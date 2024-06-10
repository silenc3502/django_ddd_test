from django.db import models
from .role_type import RoleType

class AccountRoleType(models.Model):
    role_type = models.CharField(max_length=100)

    def __str__(self):
        return self.role_type

    class Meta:
        db_table = 'account_role_type'
        app_label = 'account'
