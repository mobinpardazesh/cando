from django.urls import path
from . import views
app_name="cando"
urlpatterns = [
    path('', views.Home.as_view(),name="home"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),

]

