from django.urls import path
from .views import link_list
from . import views 
from .views import superuser_login_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.link_list, name='link_list'),
    path('add/', views.add_link, name='add_link'),
    path('edit/<int:pk>/', views.edit_link, name='edit_link'),
    path('delete/<int:pk>/', views.delete_link, name='delete_link'),
    path('login/', views.superuser_login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
