from django.urls import path,include
from . import views
app_name ='bbs'
urlpatterns = [
    #/bbs/
    path('', views.index, name='index' ),
    #/bbs/community/1
    path('community/<int:pk>/', views.CommunityDetail, name='community_detail'),
    #/bbs/posts/1
    path('post/<int:pk>/', views.PostDetail, name='post_detail'),
    path('add_post/', views.post_add, name='post_add'),



    #/bbs/register/
    path('register/', views.register, name='register')

]