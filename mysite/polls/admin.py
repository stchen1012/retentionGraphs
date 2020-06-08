from django.contrib import admin
from polls.models import Mytable
from django.apps import apps
#from polls.models import MyModel

# Register your models here.

admin.site.register(Mytable)
#admin.site.register(MyModel)
'''
models = apps.get_models()

for model in models:
    admin.site.register(model)
    '''