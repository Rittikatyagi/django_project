from django.urls import path,include
from . import views
from .views import PostListView
from .views import UserPostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView


urlpatterns = [
    # path('',views.home,name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    

       
]
