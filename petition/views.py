from django.shortcuts import render
from django.shortcuts import redirect
from .forms import PetitionForm
from .models import petition_entry
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.


def petition(request):
    count = petition_entry.objects.all().count()
    count = int(count)+5321
    remaining = int(10000-count)
    percent = int((count*100)/10000)


    if request.method =='POST':
        form = PetitionForm(request.POST)
        if form.is_valid():
            form.save()

            # messages.success(request, "Successfully Created")
            return render(request,'petition_html/petition_success.html', {'count':count, 'percent':percent, 'remaining':remaining})

            # return redirect('petition_index')
    return render(request, 'petition_html/index.html', {'count':count,'percent':percent,'remaining':remaining})

# def success(request):
#
#     return render(request, 'petition_html/petition_success.html')
