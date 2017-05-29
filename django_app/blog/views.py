from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    # return HttpResponse('<html><body>Post List</body</html>')
    # posts = Post.objects.all()
    # print(posts)
    posts = Post.objects.filter(published_date__lte=timezone.now())
    context = {
        'title' : "PostList from post_list view",
        'posts' : posts,
    }
    return render(request, 'blog/post_list.html',context=context)