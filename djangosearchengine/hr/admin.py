from django.contrib import admin
from hr.models import Employee, Organization


class OrganizationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Organization, OrganizationAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Employee, EmployeeAdmin)
