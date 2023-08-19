from django.urls import path
from . import views
urlpatterns = [
    # path('', views.Home.as_view(),name="home"),
    path('signup/', views.sign_up, name="signup"),
    path('login/', views.sign_in, name="login"),
    # path('check-email/', views.check_email, name="check-email"),
    # path('forget-password/', views.forget_password, name="forget_password"),
    # path('reset-password/', views.reset_password, name="reset_password"),

]
