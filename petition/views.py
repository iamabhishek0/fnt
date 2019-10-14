from django.shortcuts import render
from .forms import PetitionForm
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.


def petition(request):
    if request.method == 'POST':
        form = PetitionForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "Successfully Created")
            return HttpResponseRedirect('/')



    return render(request,'petition_html/index.html')