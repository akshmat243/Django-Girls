from django.shortcuts import render, redirect
from .models import Blog
from .forms import PostForm

# Create your views here.
def index_view(request):
    blogs = Blog.objects.all().order_by('created_at')
    return render(request, 'index.html', {'blogs': blogs})

def add_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
        return render(request, 'add_post.html', {'form': form})
    
    
def edit_post_view(request, pk):
    post = Blog.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = PostForm(instance=post)
    return render(request, 'add_post.html', {'form': form, 'post': post})

def post_view(request, pk):
    blog = Blog.objects.get(pk=pk)
    return render(request, 'post.html', {'blog': blog})