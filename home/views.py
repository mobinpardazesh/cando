from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

# class Home(TemplateView):
#     template_name = "home.html"
def home(request):
    return render(request, template_name="home.html", context={"home": home})

