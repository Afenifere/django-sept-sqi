from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
     # return HttpResponse("<h1>Welcome to the about page</h1>")
    return render(request, "pages/about.html")
