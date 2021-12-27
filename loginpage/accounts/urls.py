from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('about/', views.about, name="about"),
    path('TableRes/', views.TableRes, name="TableRes"), 
    path('Contactus/', views.Contactus, name="Contactus"),
    path('receipt/', views.receipt, name="receipt")
]