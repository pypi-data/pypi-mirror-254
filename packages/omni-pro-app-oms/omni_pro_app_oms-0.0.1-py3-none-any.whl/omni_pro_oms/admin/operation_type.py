from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from omni_pro_base.admin import BaseAdmin

from omni_pro_oms.forms import OperationTypeAdminForm
from omni_pro_oms.models import OperationType


class OperationTypeAdmin(BaseAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code")
    form = OperationTypeAdminForm

    def __init__(self, *args, **kwargs):
        super(OperationTypeAdmin, self).__init__(*args, **kwargs)
        self.fieldsets = ((_("Required Information"), {"fields": ("name", "code")}),) + self.fieldsets


admin.site.register(OperationType, OperationTypeAdmin)
