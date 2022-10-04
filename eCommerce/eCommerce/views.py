from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .forms import LoginForm,RegisterForm,ContactForm
from django.contrib import messages
import datetime

def home_page(request):
    context = {'title': "Home",
               'content': 'This is HomePage'}

   # request.session['page_name'] = 'visited'
   # request.session['username']=request.user.username
    return render(request,'home.html', context)

def about_page(request: object):
    context = {'title': "about",
               'content': 'This is About'}
    """
    if request.session.get('page_name'):
        print ('visited')

    if request.session.get('username'):
        print ( request.session.get('username'))
        """
   # if request.session.test_cookie_worked():
        #print("cookie tested")
        #request.session.delete_test_cookie()
        #if request.session.test_cookie_worked():
         #   pass
       # else:
        #    print('cookie deleted')
    return render(request, 'home.html', context)

def contact_page(request):
    form = ContactForm(request.POST or None)
    context = {
        "title": "Contact",
        "content": " Welcome to the contact page.",
        "form": form,
    }
    if form.is_valid():
        print (form.cleaned_data)
        return redirect('home')

    return render(request,'contact/contact_form.html',context)





def login_page(request):
    form = LoginForm(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            print (username)
            print ('login')
            login(request,user)
            context['form'] = LoginForm()
            return redirect('/')
        else:
            messages.error(request,'username or password is not correct')

    return render(request,'auth/login.html', context)

def register_page(request):

    form = RegisterForm(request.POST or None)
    print (form.is_valid())
    print (str(form.errors))

    if form.is_valid():
        print (form.cleaned_data)
        username = form.cleaned_data.get('username')
        print(username)
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        print(password,email)
        new_user = User.objects.create_user(username=username, password=password, email=email)
        new_user.save()
        messages.success(request,"Registration successful")
        return redirect('login')


    context = {'form': form}
    return render(request,'auth/register.html', context)





