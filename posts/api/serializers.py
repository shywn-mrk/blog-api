from rest_framework import serializers
from posts.models import Post, Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'parent']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'category', 'summary', 'description', 'date', 'image']

    def get_category(self, post):
        serializer = CategorySerializer(post.category)
        return serializer.data
