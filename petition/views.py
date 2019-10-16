from django.shortcuts import render
from django.shortcuts import redirect
from .forms import PetitionForm,RescueForm
from .models import petition_entry,rescue_entry
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.


def petition(request):
    count = petition_entry.objects.all().count()
    count = int(count)+3427
    remaining = int(8000-count)
    percent = int((count*100)/8000)


    if request.method =='POST':
        # form = PetitionForm(request.POST)
        # if form.is_valid():
        #     form.save()
        name = request.POST["name"]
        phone_number = request.POST["phone_number"]
        reason = request.POST["reason"]
        have_pet = request.POST["have_pet"]

        petition = petition_entry(name = name, phone_number= phone_number, reason=reason, have_pet= have_pet)
        petition.save()

            # messages.success(request, "Successfully Created")
        return render(request,'petition_html/petition_success.html', {'count':count, 'percent':percent, 'remaining':remaining})

            # return redirect('petition_index')
    return render(request, 'petition_html/index.html', {'count':count,'percent':percent,'remaining':remaining})

def rescue(request):
    if request.method =='POST':
        # ['name', 'phone_number', 'email', 'address', 'scenario', 'identification_mark', 'dog_type', ]

        # if form.is_valid():
        #     form.save()

        name = request.POST["name"]
        phone_number = request.POST["phone_number"]
        email=request.POST["email"]
        address = request.POST["address"]
        scenario = request.POST["scenario"]
        identification_mark = request.POST["identification_mark"]
        dog_type = request.POST["dog_type"]

        rescue = rescue_entry(name=name,phone_number=phone_number,email=email,address=address,scenario=scenario,identification_mark=identification_mark,dog_type=dog_type)
        rescue.save()



        return render(request, 'petition_html/rescue.html')

    return render(request, 'petition_html/rescue.html')
