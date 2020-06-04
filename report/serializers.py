from rest_framework.serializers import ModelSerializer

from .models import *


class UsersDetailsSerializers(ModelSerializer):

    class Meta:
        model = UsersDetails
        exclude = ('active',)


class UsersGetSerializers(ModelSerializer):

    class Meta:
        model = UsersDetails
        fields = ('name', 'email', 'mobile_number')
