from django.shortcuts import render,redirect
from .forms import ContactForm
from django.http import JsonResponse,HttpResponse
import datetime

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
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
        if is_ajax(request):
            return JsonResponse({'message':'Thank you!'})

    if form.errors:
        errors = form.errors.as_json()
        if is_ajax(request):
            return HttpResponse(errors,status=400,content_type='application/json')


    return render(request,'contact/contact_form.html',context)





