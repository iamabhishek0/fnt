from django.contrib import admin
from .models import petition_entry,rescue_entry


# Register your models here.
admin.site.register(petition_entry)

admin.site.register(rescue_entry)