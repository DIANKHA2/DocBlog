from django.urls import  path
from posts.views import BlogPost, BlogHome, BlogPostCreate, BlogPostUpdate, BlogPostDetail, BlogPostDelete

app_name = "posts"

urlpatterns =[
    #list
    path('', BlogHome.as_view(), name='home'),
    #create
    path('create/', BlogPostCreate.as_view(), name='create'),
    #check
    path('<str:slug>/', BlogPostDetail.as_view(), name='post'),
    #edit
    path('edit/<str:slug>/', BlogPostUpdate.as_view(), name='edit'),
    #delete
    path('delete/<str:slug>/', BlogPostDelete.as_view(), name='delete'),

]