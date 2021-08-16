from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('user/<str:username>/', views.UserPostListView.as_view(), name='user-posts'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/delete/<int:pk>', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/update/<int:pk>', views.PostUpdateView.as_view(), name='post-update')
]
