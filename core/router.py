from rest_framework import routers

from posts.api.viewsets import CategoryViewSets, PostViewSets

router = routers.DefaultRouter()

router.register('category', CategoryViewSets, basename='category')
router.register('posts', PostViewSets, basename='posts')
