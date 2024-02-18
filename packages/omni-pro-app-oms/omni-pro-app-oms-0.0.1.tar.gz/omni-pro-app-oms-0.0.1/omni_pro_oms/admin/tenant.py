from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from omni_pro_base.admin import BaseAdmin

from omni_pro_oms.forms import TenantAdminForm
from omni_pro_oms.models import Tenant


class TenantAdmin(BaseAdmin):
    list_display = ("name", "description", "code", "client_id", "client_secret")
    search_fields = ("name", "code")
    form = TenantAdminForm

    def __init__(self, *args, **kwargs):
        super(TenantAdmin, self).__init__(*args, **kwargs)
        self.fieldsets = (
            (_("Required Information"), {"fields": ("name", "description", "code", "client_id", "client_secret")}),
        ) + self.fieldsets


admin.site.register(Tenant, TenantAdmin)
