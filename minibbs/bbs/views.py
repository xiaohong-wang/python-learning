from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Community,Post, Comment
from django.views.generic import ListView
from django.views.generic import CreateView
from .forms import CreateUserForm,CommentForm,PostForm
from django.contrib.auth import authenticate
from django.contrib import messages


# Create your views here.
def index(request):
    community_list = Community.objects.all()
    post_list = Post.objects.all()
    return render(request, 'bbs/index.html', {'community_list':community_list, 'post_list':post_list})

def CommunityDetail(request, pk):
    community_list = Community.objects.all()
    community = get_object_or_404(Community,pk=pk)
    post_list = community.post_set.all()
    return render(request,'bbs/community_detail.html', {'community_list':community_list, 'post_list':post_list,'community':community})

def PostDetail(request, pk):
    community_list = Community.objects.all()
    post = get_object_or_404(Post,pk=pk)
    comment_list = post.comment_set.all()


    if request.method =='POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.post = post
                new_comment.user = request.user
                new_comment.save()
        else:
            messages.error(request, 'Need to login  to comment')
            return redirect('login')
    form = CommentForm()
    context = {'community_list':community_list,
                'post': post,
               'comment_list':comment_list,
               'form': form}
    return render(request,'bbs/post_detail.html',context)




class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author  = self.request.user
        form.instance.community = get_object_or_404(Community, pk=self.kwargs['pk'])



def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + username)

            return redirect('login')


    return render(request, 'bbs/register.html', {'form':form})


def post_add(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('bbs:index')

    form = PostForm()
    return render(request,'bbs/post_form.html', {'form':form})
