from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Category(models.Model):

    category = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.category)


class Report(models.Model):

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    file = models.CharField(max_length=500, blank=True, null=True)
    reference_number = models.CharField(max_length=100, blank=True, null=True)

    active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)


class Comments(models.Model):

    report = models.ForeignKey(Report, null=True, blank=True, on_delete=models.SET_NULL)
    comment = models.TextField()

    active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)



class UsersDetails(User):


    name = models.CharField(max_length=250, null=True, blank=True)
    mobile_number = models.CharField(max_length=11,null=True, blank=True )
    user_type = models.CharField(max_length=50, null=True, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):

        super(UsersDetails, self).save(*args, **kwargs)