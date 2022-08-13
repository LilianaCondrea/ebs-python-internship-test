from rest_framework import viewsets
from drf_util.decorators import serialize_decorator
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from apps.blog.models import Category, Blog, Comments
from apps.blog.serializers import CategorySerializer, BlogSerializer, CommentsSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

    @serialize_decorator(CommentsSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        comments = Comments.objects.create(
            title=validated_data['title'],
            slug=validated_data['slug'],
            body=validated_data['body'],
            enabled=validated_data['enabled'],
            category=validated_data['category']
        )
        return Response(BlogSerializer(comments).data)



class BlogListView(GenericAPIView):
    serializer_class = BlogSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request):
        blogs = Blog.objects.all()

        return Response(BlogSerializer(blogs, many=True).data)

    @serialize_decorator(BlogSerializer)
    def post(self, request,):
        validated_data = request.serializer.validated_data

        blogs = Blog.objects.create(
            title=validated_data['title'],
            slug=validated_data['slug'],
            body=validated_data['body'],
            enabled=validated_data['enabled'],
            category=validated_data['category']
        )
        return Response(BlogSerializer(blogs).data)

class BlogItemView(GenericAPIView):
    serializer_class = BlogSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request, pk):
        blog = get_object_or_404(Blog.objects.filter(pk=pk))
        return Response(BlogSerializer(blog).data)
