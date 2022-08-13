from django.contrib import admin
from apps.blog.models import Blog, Category, Comments

class CommentAdmin(admin.TabularInline):
    model = Comments

@admin.site.register(Blog)
class BgProfileAdmin(admin.ModelAdmin):
    list_display = ("title", "enabled",)
    list_editable = ("enabled",)
    inlines = [CommentAdmin,]

admin.site.register(Category)