import logging

from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from .models import TenantUserAssociation


@require_POST
def switch_tenant(request):
    tenant_id = request.POST.get("tenant_id")
    if TenantUserAssociation.objects.filter(user=request.user, tenant__id=tenant_id).exists():
        request.session["current_tenant_id"] = tenant_id
        logging.log(logging.DEBUG, "User %s switched to tenant {tenant_id}", request.user)
    else:
        logging.log(logging.WARNING, "User %s tried to switch to tenant {tenant_id}", request.user)
    return redirect(request.META.get("HTTP_REFERER", "home"))
