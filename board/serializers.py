from rest_framework import serializers
from .models import Board

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['boardId', 'title', 'writer', 'content', 'regDate', 'updDate']
        read_only_fields = ['regDate', 'updDate']
