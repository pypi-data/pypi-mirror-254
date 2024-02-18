from typing import Any

from tenanet.models import TenantUserAssociation


def user_tenants(request) -> dict[str, Any]:
    if request.user.is_authenticated:
        tenants = TenantUserAssociation.objects.filter(user=request.user).values_list(
            "tenant__id", "tenant__name"
        )

        current_tenant_id = request.session.get("current_tenant_id")
        available_tenants = [{"id": str(tenant[0]), "name": tenant[1]} for tenant in tenants]

        if current_tenant_id:
            current_tenant_id = str(current_tenant_id)
            available_tenants = sorted(
                available_tenants, key=lambda x: x["id"] != current_tenant_id
            )
        return {
            "available_tenants": available_tenants,
            "current_tenant_id": current_tenant_id,
        }
    return {}
