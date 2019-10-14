from django.forms import ModelForm
from .models import petition_entry


class PetitionForm(ModelForm):
    class Meta:
        model = petition_entry
        fields = ['name', 'phone_number', 'reason', 'have_pet']

    def __init__(self, *args, **kwargs):
        super(PetitionForm, self).__init__(*args, **kwargs)
        self.fields['reason'].required = False

