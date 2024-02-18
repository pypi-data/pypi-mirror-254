import logging

from tenanet.models import Tenant

NO_TENANT_WARNING = (
    "No tenant found for user %s. "
    "This should not happen, but we'll let it slide. "
    "If you see this message, please report it to the developers."
)


def _get_tenant_id(request):
    tenant = None
    if request.user.is_authenticated:
        if request.session.get("current_tenant_id"):
            tenant = Tenant.objects.filter(
                id=request.session.get("current_tenant_id"),
                tenantuserassociation__user=request.user,
            ).first()
        else:
            tenant = Tenant.objects.filter(tenantuserassociation__user=request.user).first()
        if not tenant:
            logging.warning(NO_TENANT_WARNING, request.user)
    return tenant.id if tenant else None


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.tenant = _get_tenant_id(request)
        response = self.get_response(request)
        del request.tenant
        return response
