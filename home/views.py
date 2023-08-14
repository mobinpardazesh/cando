from django.views.generic import TemplateView # Import TemplateView



from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

class Home(TemplateView):
    template_name = "home.html"
def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})
# Create your  views here.
# def home(request):
#     # form = Customerform()
#     # if request.method == "POST":
#     #     form = Customerform(request.POST)
#     #     if form.is_valid():
#     #         form.save()
#     #     # else:
#     #     #     form = Customerform
#     #     # context = {}
#     #     # context['form'] = Customerform()
#     #
#     # context = {'form': form}
#     return render(request, "home.html", {})

