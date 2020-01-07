from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'fasid_app/views/login.html')
