from rest_framework import serializers

class KakaoUserInfoSerializer(serializers.Serializer):
    access_token = serializers.CharField()
