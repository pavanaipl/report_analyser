from django.db import models
from django.contrib.auth.models import User
# from django.contrib.postgres.fields.jsonb import JSONField as JSONBField



class Project(models.Model):

    name = models.CharField(max_length=250, null=True, blank=True)


class UsersInformation(models.Model):

    name = models.CharField(max_length=250, null=True, blank=True)
    mobile_number = models.CharField(max_length=11,null=True, blank=True )
    user_email = models.EmailField(null=True, blank=True)
    # project = JSONBField(default=list, blank=True)

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
#
#
class EmployeeInformation(models.Model):

    user = models.ForeignKey(UsersInformation, null=True, blank=True, on_delete=models.SET_NULL)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    department = models.CharField(max_length=200, blank=True, null=True)
    employee_number = models.CharField(max_length=100, blank=True, null=True)

    active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.company_name)