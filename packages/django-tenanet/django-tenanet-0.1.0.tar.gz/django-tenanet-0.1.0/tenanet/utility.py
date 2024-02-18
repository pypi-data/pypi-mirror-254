from tenanet.models import TenantUserAssociation, Tenant


def switch_tenant(request, tenant_id):
    if TenantUserAssociation.objects.filter(user=request.user, tenant__id=tenant_id).exists():
        request.session["current_tenant_id"] = tenant_id
        return True
    return False


def list_tenants(user) -> list[tuple[str, str]]:
    tenants = Tenant.objects.filter(tenantuserassociation__user=user)
    return [(str(tenant.id), tenant.name) for tenant in tenants]
