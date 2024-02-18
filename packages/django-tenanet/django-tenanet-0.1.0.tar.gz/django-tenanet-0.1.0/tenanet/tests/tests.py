import pytest
from django.core.exceptions import ObjectDoesNotExist

from tenanet.admin import User
from tenanet.management.commands.tenanet import (
    create_tenant,
    list_tenants,
    delete_tenant,
    add_user_to_tenant,
    remove_user_from_tenant,
)
from tenanet.models import Tenant, TenantUserAssociation


@pytest.mark.django_db
class TestTenanetCRUD:
    def test_create_tenant_creates_tenant_and_configuration(self):
        create_tenant("TestTenant", "TT")
        tenant = Tenant.objects.get(name="TestTenant")
        assert tenant is not None
        assert tenant.tenantconfiguration.short_name == "TT"

    def test_list_tenants_returns_all_tenants(self):
        create_tenant("TestTenant1", "TT1")
        create_tenant("TestTenant2", "TT2")
        tenants = list_tenants()
        assert len(tenants) == 2

    def test_delete_tenant_removes_tenant(self):
        tenant = create_tenant("TestTenant", "TT")
        delete_tenant(tenant.id)
        with pytest.raises(ObjectDoesNotExist):
            Tenant.objects.get(id=tenant.id)

    def test_add_user_to_tenant_adds_user(self):
        create_tenant("TestTenant", "TT")
        user = User.objects.create(email="test@example.com")
        add_user_to_tenant("TestTenant", user.email)
        tenant = Tenant.objects.get(name="TestTenant")
        assert user == TenantUserAssociation.objects.get(tenant=tenant).user

    def test_remove_user_from_tenant_removes_user(self):
        tenant = create_tenant("TestTenant", "TT")
        user = User.objects.create(email="test@example.com")
        add_user_to_tenant("TestTenant", user.email)

        tenant_user_association = TenantUserAssociation.objects.filter(tenant__name="TestTenant")
        assert user.id in tenant_user_association.values_list("user__id", flat=True)
        remove_user_from_tenant(tenant.id, user.email)
        assert user.id not in tenant_user_association.values_list("user__id", flat=True)

    def test_add_user_to_non_existent_tenant_raises_error(self):
        user = User.objects.create(email="test@example.com")
        with pytest.raises(ObjectDoesNotExist):
            add_user_to_tenant("NonExistentTenant", user.email)

    def test_create_tenant_with_existing_name_raises_error(self):
        pass

    def test_delete_non_existent_tenant_raises_error(self):
        pass

    def test_remove_user_from_non_existent_tenant_raises_error(self):
        pass
