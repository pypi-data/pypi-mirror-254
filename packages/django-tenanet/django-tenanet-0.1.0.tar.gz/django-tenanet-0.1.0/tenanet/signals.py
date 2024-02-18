from django.dispatch import receiver

from tenanet.models import TenantUserAssociation

try:
    from allauth.account.signals import user_logged_in
except ImportError:
    from django.contrib.auth.signals import user_logged_in  # noqa


@receiver(user_logged_in)
def set_tenant_session(sender, request, user, **kwargs):
    print("Setting tenant session")
    user_tenant_association = TenantUserAssociation.objects.filter(user=user).first()
    if user_tenant_association:
        request.session["current_tenant_id"] = str(user_tenant_association.tenant.id)
    else:
        # TODO: Handle cases where the user does not have an associated tenant.
        #       This shouldn't happen, but it is possible if a user is created via the
        #       admin interface.
        pass
