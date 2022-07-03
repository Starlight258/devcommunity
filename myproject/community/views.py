from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post
# Create your views here.
def home(request):
    # posts = Post.objects.all() 
    posts = Post.objects.filter().order_by('-date') #오름차순
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

