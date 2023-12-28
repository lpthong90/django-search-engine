from django.contrib.auth.models import User
from django.http import HttpResponse
from hr.models import Employee, Organization
from rest_framework import viewsets

from .serializers import EmployeeSerializer, OrganizationSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the hr index.")


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
