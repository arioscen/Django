from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
me = User.objects.get(username="iii")

# def post_list(request):
#     return render(request, 'blog/post_list.html', {})

def post_list(request):
    posts = Post.objects.all().order_by('created_date')
    # posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('published_date')
    # return render(request, 'blog/post_list.html', {'posts':posts})

    post_form = PostForm()
    return render(request, 'blog/post_list.html', locals())

def add_record(request):
    if request.POST:
        title = request.POST['title'].encode('utf-8')
        text = request.POST['text'].encode('utf-8')
        newpost = Post.objects.create(author=me,title=title,text=text)
    return redirect('/blog')

def post_record(request,id):
    post = Post.objects.get(id = id)
    return render(request, 'blog/post_record.html',locals())