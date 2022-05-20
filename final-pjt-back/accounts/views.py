from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProfileSerializer

User = get_user_model()

@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)
    
# 좋아하는 장르 출력
# genres = {}
# for genre in Genre.objects.all():
#     genres[genre.name] = 0
# user = request.user
# for review in Review.objects.filter(user=user):
#     for movie_genre in review.movie.genres.all():
#         genres[movie_genre.name] += review.score - 3

def shop(request, username):
    pass