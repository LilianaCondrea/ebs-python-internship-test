from django.urls import path

from apps.blog.views import CategoryViewSet, BlogListView, BlogItemView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'comments', CommentsViewSet, basename='comment')

urlpatterns = router.urls

urlpatterns += [
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogItemView.as_view(), name='blog_item'),
]
