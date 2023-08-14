from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView

class Home(TemplateView):
    template_name = "home.html"


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

