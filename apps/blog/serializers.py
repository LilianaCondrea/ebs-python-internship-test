from rest_framework import serializers

from apps.blog.models import Category, Blog, Comments


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    # comments = CommentsSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'
        # fields = ['title', 'slug', 'body', 'posted', 'category', 'enabled', 'comments']
