from django.shortcuts import render, redirect
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        
        Post.objects.create(
            title=title,
            content=content,
            author=author
        )
        return redirect('post_list')
    
    return render(request, 'blog/add_post.html')