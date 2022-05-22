from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import ProfileSerializer, UserSerializer

User = get_user_model()

@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)
    

def shop(request, username):
    pass


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)