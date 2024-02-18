from django.apps import apps
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import Tenant, TenantUserAssociation, TenantConfiguration

User = get_user_model()
TenantMetaModel = apps.get_model(settings.TENANET_TENANT_META_MODEL, require_ready=False)


class TenantUserAssociationInline(admin.TabularInline):
    model = TenantUserAssociation
    extra = 1


class TenantConfigurationInline(admin.TabularInline):
    model = TenantConfiguration
    extra = 1
    min_num = 1


class TenantMetaInline(admin.StackedInline):
    model = TenantMetaModel
    fk_name = "tenant"
    min_num = 1


class CustomUserAdmin(UserAdmin):
    inlines = (TenantUserAssociationInline,)


class TenantConfigurationAdmin(admin.ModelAdmin):
    list_display = ("tenant", "short_name")
    list_filter = ("tenant", "short_name")
    search_fields = ("tenant__name", "short_name")


class TenantUserAssociationAdmin(admin.ModelAdmin):
    list_display = ("user", "tenant")
    list_filter = ("tenant",)
    search_fields = ("user__email", "user__email", "tenant__name")


class TenantAdmin(admin.ModelAdmin):
    list_display = ("name", "id")
    search_fields = ("name", "id")
    readonly_fields = ("id",)

    inlines = (TenantUserAssociationInline, TenantConfigurationInline, TenantMetaInline)


admin.site.register(Tenant, TenantAdmin)
admin.site.register(TenantUserAssociation, TenantUserAssociationAdmin)

admin.site.register(TenantConfiguration, TenantConfigurationAdmin)
