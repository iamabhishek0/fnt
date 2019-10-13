from django.shortcuts import render

# Create your views here.


def petition(request):
    return render(request,'petition_html/index.html')