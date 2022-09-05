from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.blog.views import CategoryViewSet, BlogListView, BlogItemView, CreatePostView, CreateCommentView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = router.urls

urlpatterns += [
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogItemView.as_view(), name='blog_item'),
    path('blog/add', CreatePostView.as_view(), name='add_blog_post'),
    path('blog/comment', CreateCommentView.as_view(), name='add_comment')
]
