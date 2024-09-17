from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('login/', auth_views.LoginView.as_view(next_page='post_list'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='post_list'), name='logout'),
    path('register/', views.register, name='register'),
    path('post_create/', views.create_post, name='create_post'),
    path('post/<int:post_id>/edit/', views.edit_post, name='post_edit'),
    path('post/<int:post_id>/delete/', views.delete_post, name='post_delete'),

]
