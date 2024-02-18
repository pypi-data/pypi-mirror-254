from django.urls import path

from .views import switch_tenant

app_name = "tenanet"
urlpatterns = [
    path("switch_tenant/", switch_tenant, name="switch_tenant"),
]
