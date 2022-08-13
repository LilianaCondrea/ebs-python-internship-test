from django.contrib.auth.models import User
from django.db.models import fields
from django.utils import tree
from rest_framework import serializers

from apps.blog.models import Category, Blog, Comments


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['text', 'blog']


class BlogSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, read_only=True)
    class Meta:
        model = Blog
        # fields = '__all__'
        fields = ['title', 'slug', 'body', 'posted','category', 'enabled', 'comments']