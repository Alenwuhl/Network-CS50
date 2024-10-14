
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('toggle_follow/<str:username>/', views.toggle_follow, name='toggle_follow'),
    path("newPost", views.newPost, name="newPost"),
    path("allPosts", views.allPosts, name="allPosts"),
    path("following", views.following, name="following"),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
]
