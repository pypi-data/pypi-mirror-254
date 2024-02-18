import pytest
from django.core.management import BaseCommand

from tenanet.admin import User
from tenanet.models import Tenant, TenantConfiguration


@pytest.mark.django_db
def create_tenant(name, short_name):
    tenant = Tenant.objects.create(name=name)
    tenant.save()
    TenantConfiguration.objects.create(tenant=tenant, short_name=short_name).save()
    print(f"Created tenant {name} with id {tenant.id} and short name {short_name}")
    return tenant


def list_tenants():
    tenants = Tenant.objects.all()
    [
        print(f"{tenant.id} - {tenant.name} - {tenant.tenantconfiguration.short_name}")
        for tenant in tenants
    ]
    return tenants


def delete_tenant(tenant_id):
    Tenant.objects.get(id=tenant_id).delete()
    print(f"Deleted tenant {tenant_id}")


def add_user_to_tenant(tenant_name, user):
    Tenant.objects.get(name=tenant_name).add_user(User.objects.get(email=user))
    print(f"Added user {user} to tenant {tenant_name}")


def remove_user_from_tenant(tenant_id, user):
    Tenant.objects.get(id=tenant_id).remove_user(User.objects.get(email=user))
    print(f"Removed user {user} from tenant {tenant_id}")


class Command(BaseCommand):
    help = """
    Manage tenants in the system.
    """

    def add_arguments(self, parser):
        parser.add_argument(
            "command",
            choices=["create", "list", "delete", "add-user", "remove-user"],
            help="Command to run",
        )
        parser.add_argument(
            "--name",
            dest="name",
            default=None,
            type=str,
            help="Name of the tenant to create",
        )
        parser.add_argument(
            "--short-name",
            dest="short_name",
            default=None,
            type=str,
            help="Short name of the tenant to create",
        )

        parser.add_argument(
            "--user",
            dest="user",
            default=None,
            type=str,
            help="Email of a user to add/remove to a tenant",
        )

    @pytest.mark.django_db
    def handle(self, *args, **options):
        command = options["command"]
        if command == "create":
            create_tenant(options["name"], options["short_name"])
        elif command == "delete":
            delete_tenant(options["name"])
        elif command == "add-user":
            add_user_to_tenant(options["name"], options["user"])
        elif command == "remove-user":
            remove_user_from_tenant(options["name"], options["user"])
        elif command == "list":
            list_tenants()
