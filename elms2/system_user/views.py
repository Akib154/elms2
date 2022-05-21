from django.shortcuts import render

# Create your views here.

def getUser(request):
    return render(request,'user.html')
