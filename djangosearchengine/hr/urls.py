from rest_framework import routers

from . import views

app_name = "hr"

router = routers.DefaultRouter()
router.register(r"organizations", views.OrganizationViewSet)
router.register(r"employees", views.EmployeeViewSet)

urlpatterns = router.urls
