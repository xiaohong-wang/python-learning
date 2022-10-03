from django.urls import path
from . import views
from .views import BloggerListView, BlogDetailView,BloggerDetailView

app_name = 'blog'
urlpatterns =[
    #/blog/
    path('', views.index, name='index' ),
    #/blog/1/
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    #/blog/1/add_comment/
    path('<int:pk>/add_comment/', views.CommentFormView, name='add_comment'),

    #/blog/bloggers/
    path('bloggers/', BloggerListView.as_view(), name='all_bloggers'),
    #/blog/bloggers/1/
    path('bloggers/<int:pk>/', BloggerDetailView.as_view(), name='blogger_detail'),

    #/blog/register/
    path('register/', views.register, name='register'),

    #/blog/login/
    path('login/', views.loginPage, name='login'),
    #/blog/logout/
    path('logout/', views.logoutUser, name='logout')


]