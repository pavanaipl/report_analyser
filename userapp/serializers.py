from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers
from django.shortcuts import get_object_or_404

class UsersInformationSerializers(ModelSerializer):

    class Meta:
        model = UsersInformation
        exclude = ('active',)

class GetUsersInformationSerializers(ModelSerializer):

    project = serializers.SerializerMethodField('fetch_project_details')

    def fetch_project_details(self, instance):
        project_details = []
        for project in instance.project:
            try:
                project_obj = get_object_or_404(Project, id=project["project"])
                project["project"] = {"id":project_obj.id, "name":project_obj.name}
                project_details.append(project)
            except:
                pass
        return project_details

    class Meta:
        model = UsersInformation
        exclude = ('active',)




class EmployeeInformationSerializers(ModelSerializer):

    class Meta:
        model = EmployeeInformation
        exclude = ('active',)

class GetEmployeeInformationSerializers(ModelSerializer):
    user = serializers.SerializerMethodField('user_details')

    def user_details(self, instance):
        data = {"id":instance.user.id, "name":instance.user.name, "mobile_number":
            instance.user.mobile_number}
        return data


    class Meta:
        model = EmployeeInformation
        exclude = ("active",)