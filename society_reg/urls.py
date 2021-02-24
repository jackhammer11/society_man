from . import views
from django.urls import path
from django.conf.urls import url
 


urlpatterns = [
    path('',views.home,name="home"),
    path('registration/',views.register,name="reg"),
    path('visitor/',views.visitor,name="visitor"),
    path('visitorList/', views.visitorList),
    path('userList/', views.societyList),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('visitordetails/<int:pk>/', views.visitordetails),
    path('login/', views.login_view,name='login'),

] 
