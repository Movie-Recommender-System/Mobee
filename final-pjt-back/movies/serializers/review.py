from random import choices
from django.forms import IntegerField
from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Review

User = get_user_model()

class ReviewSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')
    
    score = serializers.IntegerField(max_value=5, min_value=1)  # 범위 지정 1,2,3,4,5
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)
    like_count = serializers.IntegerField(source='like_users.count', read_only=True)
    class Meta:
        model = Review
        fields = ('pk', 'user', 'movie', 'content', 'score', 
        'created_at', 'updated_at', 'like_count', 'like_users', 'like_count')
        read_only_fields = ('movie', )