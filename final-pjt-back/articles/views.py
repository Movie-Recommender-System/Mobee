from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.core.paginator import Paginator

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Article, Comment
from .serializers.article import ArticleListSerializer, ArticleSerializer
from .serializers.comment import CommentSerializer

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def article_list_or_create(request):

    def article_list():
        # comment 개수 추가
        articles = Article.objects.annotate(
            comment_count=Count('comments', distinct=True),
            like_count=Count('like_users', distinct=True)
        ).order_by('-pk')
        
        paginator = Paginator(articles, 10)
        page_num = request.GET.get('page')
        page_obj = paginator.get_page(page_num)
        serializer = ArticleListSerializer(page_obj, many=True)
        data = {}
        data['count'] = articles.count()
        data['articles'] = serializer.data
        return Response(data)
    

    def create_article():
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return article_list()
    elif request.method == 'POST':
        return create_article()


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def article_detail_or_update_or_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user
    def article_detail():
        serializer = ArticleSerializer(article)
        data = serializer.data
        if article.like_users.filter(pk=user.pk).exists():
            data['is_liked'] = True
        else:
            data['is_liked'] = False
        return Response(data)

    def update_article():
        if user == article.user:
            serializer = ArticleSerializer(instance=article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        return Response(['작성한 사용자만 수정 권한이 있습니다.'], status=status.HTTP_403_FORBIDDEN)
    def delete_article():
        if user == article.user or user.is_staff == True:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(["관리자나 작성한 사용자만 삭제할 권한이 있습니다."], status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        return article_detail()
    elif request.method == 'PUT':
        return update_article()
    elif request.method == 'DELETE':
        return delete_article()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user
    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
    else:
        article.like_users.add(user)
    serializer = ArticleSerializer(article)
    data = serializer.data
    if article.like_users.filter(pk=user.pk).exists():
        data['is_liked'] = True
    else:
        data['is_liked'] = False
    return Response(data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request, article_pk):
    user = request.user
    article = get_object_or_404(Article, pk=article_pk)
    
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user=user)

        # 기존 serializer 가 return 되면, 단일 comment 만 응답으로 받게됨.
        # 사용자가 댓글을 입력하는 사이에 업데이트된 comment 확인 불가 => 업데이트된 전체 목록 return 
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_update_or_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    def update_comment():
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = article.comments.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)
        return Response(['작성한 사용자만 수정 권한이 있습니다.'], status=status.HTTP_403_FORBIDDEN)

    def delete_comment():
        if request.user == comment.user or request.user.is_staff == True:
            comment.delete()
            comments = article.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
        return Response(["관리자나 작성한 사용자만 삭제할 권한이 있습니다."], status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PUT':
        return update_comment()
    elif request.method == 'DELETE':
        return delete_comment()