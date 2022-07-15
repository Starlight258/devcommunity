from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm, FreePostForm, FreeCommentForm
from .models import Post, FreePost
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    # posts = Post.objects.all() 
    posts = Post.objects.filter().order_by('-date') #오름차순
    paginator = Paginator(posts, 5) #5개씩 끊어서
    pagenum = request.GET.get('page') #page가져오기
    posts= paginator.get_page(pagenum)
    return render(request, 'index.html', {'posts':posts})

def postcreate(request):
    #request method가 POST일 경우 입력값 저장
    if request.method == 'POST' or request.method== 'FILES':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('home')
    #GET일 경우 form 입력 html 띄우기
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form':form})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    return render(request, 'detail.html', {'post_detail':post_detail, 'comment_form':comment_form})

#댓글 저장
def new_comment(request, post_id): 
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post= get_object_or_404(Post, pk=post_id) #외래키까지 저장하고 저장
        finished_form.save()
    return redirect('detail', post_id)

#----------------------------------------------------------------------------------------------
# 자유게시판
def freehome(request):
    # posts = Post.objects.all() 
    posts = FreePost.objects.filter().order_by('-date') #오름차순
    return render(request, 'free_index.html', {'posts':posts})

def freepostcreate(request):
    #request method가 POST일 경우 입력값 저장
    if request.method == 'POST' or request.method== 'FILES':
        form = FreePostForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.author = request.user
            unfinished.save() 
            return redirect('freehome')
    #GET일 경우 form 입력 html 띄우기
    else:
        form = FreePostForm()
    return render(request, 'free_post_form.html', {'form':form})

def freedetail(request, post_id):
    post_detail = get_object_or_404(FreePost, pk=post_id)
    comment_form = FreeCommentForm()
    return render(request, 'free_detail.html', {'post_detail':post_detail, 'comment_form':comment_form})

#댓글 저장
def new_freecomment(request, post_id): 
    filled_form = FreeCommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post= get_object_or_404(FreePost, pk=post_id) #외래키까지 저장하고 저장
        finished_form.author = request.user
        finished_form.save()
    return redirect('freedetail', post_id)


