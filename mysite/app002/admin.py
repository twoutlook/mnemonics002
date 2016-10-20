from django.contrib import admin

# Register your models here.

# Requirements
# command line : pip install django-import-export
# mysite/settings: 
# INSTALLED_APPS = [
#     'import_export',
#     'app001',

from import_export import resources
from import_export.admin import ImportExportModelAdmin


# My Project
from .models import Mnemonics


class MnemonicsResource(resources.ModelResource):
    class Meta:
        model = Mnemonics

class MnemonicsAdmin(ImportExportModelAdmin):
    resource_class = MnemonicsResource
admin.site.register(Mnemonics,MnemonicsAdmin)




