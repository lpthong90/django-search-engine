from django.contrib.auth.models import User
from hr.models import Employee, Organization
from rest_framework import serializers


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="hr:organization-detail")

    class Meta:
        model = Organization
        fields = ["id", "url", "name"]
        ordering = "-id"


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="hr:employee-detail")

    class Meta:
        model = Employee
        fields = [
            "id",
            "url",
            "first_name",
            "last_name",
            "contact_info",
            "department",
            "position",
            "location",
            "status",
        ]
        ordering = "-id"
