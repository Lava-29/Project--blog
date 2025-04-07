from django.shortcuts import render
from lava_app.models import Post

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)
# Create your views here.
