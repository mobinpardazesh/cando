from django.urls import path
from . import views
urlpatterns = [
    # path('', views.Home.as_view(),name="home"),
    path('', views.bloglist, name="signup"),
    path('post/', views.blogpost, name="login"),
    path('postdescription/', views.blogpostdescription, name="logout"),

    # path('check-email/', views.check_email, name="check-email"),
    # path('forget-password/', views.forget_password, name="forget_password"),
    # path('reset-password/', views.reset_password, name="reset_password"),

]