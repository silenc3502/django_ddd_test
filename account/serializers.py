from rest_framework import serializers
from entity.profile import Profile

class AccountRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    nickname = serializers.CharField(max_length=100, required=True)
