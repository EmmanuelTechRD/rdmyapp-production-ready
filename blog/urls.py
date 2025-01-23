from django.urls import path
from . import views

urlpatterns = [
    # Blog:
    path('', views.post_view, name='post_list'),
    path('create/', views.create_post_view, name='create_post'),
    path('update/<int:pk>/', views.update_post_view, name='update_post'),
    path('delete/<int:pk>/', views.delete_post_view, name='delete_post'),
    
    # User:
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    
    # App:
    path('about/', views.about_view, name='about'),
]
