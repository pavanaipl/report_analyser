from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(UsersInformation)
admin.site.register(EmployeeInformation)
admin.site.register(Project)
