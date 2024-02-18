from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from omni_pro_base.admin import BaseAdmin

from omni_pro_oms.forms import OperationAdminForm
from omni_pro_oms.models import Operation


class OperationAdmin(BaseAdmin):
    list_display = ("name", "destination", "score", "endpoint_url", "timeout")
    list_filter = ("destination", "http_method")
    search_fields = ("name", "endpoint_url")
    form = OperationAdminForm

    def __init__(self, *args, **kwargs):
        super(OperationAdmin, self).__init__(*args, **kwargs)
        self.fieldsets = (
            (
                _("Required Information"),
                {"fields": ("name", "destination", "score", "endpoint_url", "http_method", "timeout", "auth_type")},
            ),
            (_("Optional Information"), {"fields": ("headers",)}),
        ) + self.fieldsets


admin.site.register(Operation, OperationAdmin)
