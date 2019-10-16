from django.forms import ModelForm
from .models import petition_entry,rescue_entry


class PetitionForm(ModelForm):
    class Meta:
        model = petition_entry
        fields = ['name', 'phone_number', 'reason', 'have_pet']

    def __init__(self, *args, **kwargs):
        super(PetitionForm, self).__init__(*args, **kwargs)
        self.fields['reason'].required = False

class RescueForm(ModelForm):
    class Meta:
        model = rescue_entry
        fields = ['name', 'phone_number','email', 'address', 'scenario', 'identification_mark' ,'dog_type',]

    def __init__(self, *args, **kwargs):
        super(RescueForm, self).__init__(*args, **kwargs)
        self.fields['scenario'].required = False
        self.fields['identification_mark'].required = False
