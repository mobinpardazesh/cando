from django.urls import path
from . import views
app_name="cando"
urlpatterns = [
    path('', views.Home.as_view(),name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('check-email/', views.check_email, name="check-email"),
    path('forget-password/', views.forget_password, name="forget-password"),
    path('reset-password/', views.reset_password, name="reset-password"),

]

