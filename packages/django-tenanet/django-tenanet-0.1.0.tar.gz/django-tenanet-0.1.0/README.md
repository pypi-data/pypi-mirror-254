django-tenanet
=======

Tenanet is a simple multi-tenancy framework for Django.
It features a simple tenant data model, a middleware to handle tenant 
resolution, a context processor and a query manager to handle tenant data 
isolation.

Works well with django-allauth or other custom User models. TenantUser 
association is inlined in the default User admin form and the default User 
serializer.

A swappable Tenant metaclass is provided to allow for custom metadata 
(e.g. app-specific preferences, filters, feature flags, etc.) to be added to 
the Tenants.

## Features
* Tenant data model
* Tenant middleware
* Tenant query manager
* Swappable Tenant metaclass

## Requirements (tested)
* Python 3.6+
* Django 4.0+

## Installation
pip install django-tenanet

## Usage
### Settings
Add tenanet to your INSTALLED_APPS:
```python
INSTALLED_APPS = (
    ...
    'tenanet',
)
```
Add tenanet.middleware.TenantMiddleware to your MIDDLEWARE_CLASSES:
```python
MIDDLEWARE_CLASSES = (
    ...
    'tenanet.middleware.TenantMiddleware',
)
```
Override the TENANET_TENANT_MODEL setting to point to your custom tenant model:
```python
TENANET_TENANT_MODEL = 'myapp.MyTenantModel'
```
### Models
#### TenantMeta
```python
from tenanet.models import BaseTenantMeta

class MyTenantMeta(BaseTenantMeta):
    # Add custom tenant metadata fields here
```
#### Tenant scoped data with TenantDataModel
```python
from tenanet.models import TenantDataModel

class MyTenantModel(TenantDataModel):
    # Add custom tenant data model fields here
```
### Admin
#### TenantUser inline
```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from tenanet.admin import TenantUserAssociationInline

class MyUserAdmin(UserAdmin):
    # your user admin config here
    inlines = (TenantUserAssociationInline,)

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
```

# License
This project is licensed under the terms of the Django-Tenanet Limited Use License.
See the LICENSE file for license rights and limitations.
