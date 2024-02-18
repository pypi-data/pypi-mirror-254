from django.db import models


class TenantQuerySet(models.QuerySet):
    def for_tenant(self, tenant) -> models.QuerySet:
        return self.filter(tenant=tenant)


class TenantManager(models.Manager):
    def get_queryset(self) -> TenantQuerySet:
        return TenantQuerySet(self.model, using=self._db)

    def for_tenant(self, tenant) -> models.QuerySet:
        return self.get_queryset().for_tenant(tenant)
