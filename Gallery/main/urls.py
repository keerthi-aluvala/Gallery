from django.urls import path
from . import views
from .views import (
	PostListView, 
	PostDetailView, 
	PostCreateView, 
	PostUpdateView,
	PostDeleteView,
)

urlpatterns = [
    #path('',views.home,name='Gallery-home'),
    path('', PostListView.as_view() , name='Gallery-home'),
    path('search',views.search,name='search'),
    path('show/<int:pk>/', PostDetailView.as_view() , name='post-detail'),
    #path('create/', views.create_blog_view, name='post-create'),
    path('post/new/', PostCreateView.as_view() , name='post-create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view() , name='post-update'),
    #path('post/<int:pk>/edit/', views.edit_blog_view, name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view() , name='post-delete'),
]
