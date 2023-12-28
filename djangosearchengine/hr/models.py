from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name}"


class Employee(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    contact_info = models.CharField(max_length=150)

    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="employees", null=False
    )
    department = models.CharField(max_length=150, null=True, blank=True)
    position = models.CharField(max_length=150, null=True, blank=True)
    location = models.CharField(max_length=40, null=True, blank=True)

    STATUS_CHOICES = (
        ("active", "Active"),
        ("not_started", "Not started"),
        ("terminated", "Terminated"),
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default="active")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
