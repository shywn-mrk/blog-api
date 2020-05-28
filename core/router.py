from rest_framework import routers

from posts.api.viewsets import CategoryViewSets, PostViewSets

router = routers.DefaultRouter()

router.register('categories', CategoryViewSets, basename='categories')
router.register('posts', PostViewSets, basename='posts')
