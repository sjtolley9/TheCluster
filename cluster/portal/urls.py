from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.create_job, name='create'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]