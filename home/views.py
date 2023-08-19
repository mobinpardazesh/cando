from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import Check_Email_Form, Forget_Password_Form, Reset_Password_Form
from .forms import SignUpForm ,Login_Form


# class Home(TemplateView):
#     template_name = "home.html"
def home(request):
    return render(request, template_name="home.html", context={"home": home})

