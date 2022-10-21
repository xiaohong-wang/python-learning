from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm, GuestForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import  GuestEmail
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings
from .signals import user_login_signal

User = get_user_model()


@login_required
def account_home(request):
    return render(request,'accounts/home.html', {})


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {'form': form}
    next_ = request.GET.get('next')

    next_post = request.POST.get('next')

    redirect_path = next_ or next_post or None

   # print(request.POST)

    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)

        if user is not None:

            login(request,user)
            user_login_signal.send(user.__class__, instance=user, request=request)
            context['form'] = LoginForm()

            try:
                del request.session['guest_id']

            except:
                pass


            if url_has_allowed_host_and_scheme(redirect_path,allowed_hosts=request.get_host()):


                return redirect(redirect_path)
            else:
                return redirect('/')

        else:
            messages.error(request,'username or password is not correct')

    return render(request,'accounts/login.html', context)

def logout_page(request):
   # print( 'logout')
    logout(request)
    return redirect('about')

def register_page(request):

    form = RegisterForm(request.POST or None)
    context = {'form': form}
    """
    if form.is_valid():

        username = form.cleaned_data.get('username')

        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
       # print(password,email)
        new_user = User.objects.create_user(username=username, password=password, email=email)
        new_user.save()
        messages.success(request,"Registration successful")
        return redirect('login')
    """
    if form.is_valid():
        form.save()
        return redirect('login')


    return render(request,'accounts/register.html', context)


def guest_register_page(request):
    form = GuestForm(request.POST or None)
    context = {'form': form}
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    #print(request.POST)

    if form.is_valid():
        email = form.cleaned_data['email']
        new_guest = GuestEmail.objects.create(email=email)
       # form.save()
        request.session['guest_id'] = new_guest.id
        #print('new guest', new_guest.id)

        if url_has_allowed_host_and_scheme(redirect_path,allowed_hosts=request.get_host()):

            return redirect(redirect_path)
        else:
            return redirect('/register/')

        #return redirect(request.META.get('HTTP_REFERER'))
    return redirect('/register/')

