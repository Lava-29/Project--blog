from django.contrib import admin
from lava_app.models import Post
class PostAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post, PostAdmin)
# Register your models here.
