from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime, timedelta
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
    created_at = serializers.SerializerMethodField('create_time')
    updated_at = serializers.SerializerMethodField('update_time')
    
    def create_time (self, my):
        time = datetime.now(tz=timezone.utc) - my.created_at
        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - my.created_at.date()
            return str(time.days) + '일 전'
        else:
            return False

    def update_time (self, my):
        time = datetime.now(tz=timezone.utc) - my.updated_at
        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - my.updated_at.date()
            return str(time.days) + '일 전'
        else:
            return False

    class Meta:
        model = Review
        fields = ('pk', 'user', 'movie', 'content', 'score', 
        'created_at', 'updated_at', 'like_count', 'like_users', 'like_count')
        read_only_fields = ('movie', )