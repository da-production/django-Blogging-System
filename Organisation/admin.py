from django.contrib import admin
from .models import Organisation, Endpoints, User
# Register your models here.
admin.site.register(Organisation)
admin.site.register(Endpoints)
admin.site.register(User)
