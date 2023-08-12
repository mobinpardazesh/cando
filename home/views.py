from django.shortcuts import render



# Create your  views here.
def home(request):
    # form = Customerform()
    # if request.method == "POST":
    #     form = Customerform(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     # else:
    #     #     form = Customerform
    #     # context = {}
    #     # context['form'] = Customerform()
    #
    # context = {'form': form}
    return render(request, "home.html", {})

