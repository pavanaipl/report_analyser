from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import ast
from django.http import QueryDict
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
from rest_framework import viewsets


class UsersInformationApi(APIView):

    def get(self, request, pk):
        user_obj = get_object_or_404(UsersInformation, id=pk, active=True)
        serializer = GetUsersInformationSerializers(user_obj)
        return Response(serializer.data, 200)

    def post(self, request, pk):
        data = QueryDict.dict(request.data)
        serializer = UsersInformationSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 201)
        return Response(serializer.errors, 400)
#
#
class EmployeeInformationApi(APIView):

    def get(self, request, pk):
        employee_obj = get_object_or_404(EmployeeInformation, id=pk, active=True)
        serializer = GetEmployeeInformationSerializers(employee_obj)
        return Response(serializer.data, 200)

    def post(self, request, pk):
        data = QueryDict.dict(request.data)
        serializer = EmployeeInformationSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 201)
        return Response(serializer.errors, 400)