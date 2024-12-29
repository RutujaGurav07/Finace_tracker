from django.contrib import admin
from tracker.models import Category, Trasaction

# Register your models here.
admin.site.register(Trasaction)
admin.site.register(Category)