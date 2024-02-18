import uuid

from django.conf import settings
from django.db import models

from tenanet.managers import TenantManager


class Tenant(models.Model):
    id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def add_user(self, user):
        TenantUserAssociation.objects.create(user=user, tenant=self)

    def remove_user(self, user):
        TenantUserAssociation.objects.filter(user=user, tenant=self).delete()


class TenantConfiguration(models.Model):
    tenant = models.OneToOneField(Tenant, on_delete=models.CASCADE)
    short_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="tenant_logos", blank=True, null=True)


class TenantUserAssociation(models.Model):
    id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "tenant")

    def __str__(self):
        return f"{self.user} - {self.tenant}"


class TenantDataModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    objects = TenantManager()

    class Meta:
        abstract = True


class BaseTenantMeta(models.Model):
    tenant = models.OneToOneField(Tenant, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        abstract = True
        swappable = "TENANET_TENANT_META_MODEL"
