from rest_framework import viewsets
from posts.models import Post, Category
from .serializers import CategorySerializer, PostSerializer

class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostViewSets(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
