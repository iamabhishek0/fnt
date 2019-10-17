from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import petition_entry,rescue_entry


# Register your models here.
# admin.site.register(petition_entry)
#
# class PetitionAdmin(admin.ModelAdmin):
#
#     list_display= ['name', 'phone_number', 'have_pet','reason', ]
#     class Meta:
#         model = petition_entry

# admin.site.unregister(petition_entry)

# @admin.register(petition_entry)
class PetitionAdmin(ImportExportModelAdmin):
    model = petition_entry
    list_display = ['name', 'phone_number', 'have_pet','reason', ]
    export_order = ['name', 'phone_number', 'have_pet','reason', ]
admin.site.register(petition_entry,PetitionAdmin)

admin.site.register(rescue_entry)