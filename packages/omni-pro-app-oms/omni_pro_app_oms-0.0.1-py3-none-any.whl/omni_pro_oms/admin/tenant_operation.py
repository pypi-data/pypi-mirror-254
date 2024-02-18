from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from omni_pro_base.admin import BaseAdmin

from omni_pro_oms.forms import TenantOperationAdminForm
from omni_pro_oms.models import TenantOperation


class TenantOperationAdmin(BaseAdmin):
    list_display = ("tenant_id", "operation_id", "operation_type_id", "config_id")
    list_filter = ("tenant_id", "operation_id", "operation_type_id", "config_id")
    search_fields = ("tenant_id", "operation_id", "operation_type_id", "config_id")
    form = TenantOperationAdminForm

    def __init__(self, *args, **kwargs):
        super(TenantOperationAdmin, self).__init__(*args, **kwargs)
        self.fieldsets = (
            (
                _("Tenant Operation"),
                {"fields": ("name", "tenant_id", "operation_id", "operation_type_id", "config_id")},
            ),
        ) + self.fieldsets


admin.site.register(TenantOperation, TenantOperationAdmin)
