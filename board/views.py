from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Post
from .forms import WriteForm
from django.shortcuts import redirect


def write(request):
    if request.user.is_authenticated:
        post = WriteForm()
        return render(request, 'write_form.html', {'form': post})
    else:
        return render(request, 'login_error.html')


def write_process(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = WriteForm(request.POST)
            if form.is_valid():
                post = Post()
                post.title = form.cleaned_data['title']
                post.content = form.cleaned_data['content']
                post.author = request.user
                post.save()
                return redirect('/board')

    return render(request, 'login_error.html')

def view_post(request):
    form = AuthenticationForm(request.user)
    if 'boardNo' in request.GET:
        post = Post.objects.filter(id=request.GET['boardNo']).first()
        if post is not None:
            return render(request, 'view_form.html', {'form':form, 'post': post})

    return render(request, 'login_error.html')

def index(request):
    form = AuthenticationForm()
    posts = Post.objects.all()
    return render(request, 'index.html', {'form': form, 'posts': posts})
