from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^user-info/((?P<pk>\d+)/)*$', UsersInformationApi.as_view()),
    url(r'^employee-info/((?P<pk>\d+)/)*$', EmployeeInformationApi.as_view()),
]