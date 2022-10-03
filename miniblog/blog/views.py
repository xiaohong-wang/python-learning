from django.shortcuts import render,redirect
from django.http import  HttpResponse
from .models import Author,Blog,Comment
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import CreateUserForm, CommentForm
from django.contrib import messages
from django.contrib.auth.forms import  AuthenticationForm

# Create your views here.

def index(request):
    blogs = Blog.objects.all()
    return render(request,'blog/index.html',{'blog_list':blogs})

class BloggerListView(generic.ListView):
    model = Author
    context_object_name = 'blogger_list'
    template_name = 'blog/all_bloggers.html'

class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'

class BloggerDetailView(generic.DetailView):
    model = Author
    template_name = 'blog/blogger_detail.html'


def CommentFormView(request, pk):
    """

    :type request: object
    """
    blog = get_object_or_404(Blog, pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit = False)
           # print (form.cleaned_data())
            new_comment.blog = blog
            new_comment.user = request.user
            new_comment.save()
            return redirect( 'blog:blog_detail',pk=pk)

    return render(request, 'blog/comment_form.html', {'form': form, 'blog': blog})


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account was created for ' + form.cleaned_data.get('username'))
            return redirect('blog:login')
    return render(request,'blog/register_form.html', {'form':form})

def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print ('valid.form')
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request, f'You are now logged in as {username}')
                return redirect('blog:index')
            else:
                messages.error(request,'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    form = AuthenticationForm()
    return render(request,'blog/login.html', {'form':form})

def logoutUser(request):
    logout(request)
    messages.info(request,'You have successfully logged out.')
    return redirect('blog:index')

