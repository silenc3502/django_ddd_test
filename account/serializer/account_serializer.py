from rest_framework import serializers

from account.entity.account import Account


class AccountSerializer(serializers.ModelSerializer):
    login_type = serializers.CharField(source='login_type.login_type', read_only=True)
    role_type = serializers.CharField(source='role_type.role_type', read_only=True)

    class Meta:
        model = Account
        fields = ['id', 'login_type', 'role_type']