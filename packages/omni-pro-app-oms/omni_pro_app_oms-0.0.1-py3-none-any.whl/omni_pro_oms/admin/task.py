from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from omni_pro_base.admin import BaseAdmin

from omni_pro_oms.forms import TaskAdminForm
from omni_pro_oms.models import Task


class TaskAdmin(BaseAdmin):
    list_display = ("tenant_id", "operation_id", "status", "url_src", "url_dst", "time")
    list_filter = ("tenant_id", "operation_id", "status")
    search_fields = ("url_src", "url_dst", "body_src", "body_dst", "time")
    form = TaskAdminForm

    def __init__(self, *args, **kwargs):
        super(TaskAdmin, self).__init__(*args, **kwargs)
        self.fieldsets = (
            (
                _("Required Information"),
                {"fields": ("name", "tenant_id", "operation_id", "status", "time")},
            ),
            (_("Source Info"), {"fields": ("body_src", "headers_src", "params_src", "response_src", "url_src")}),
            (_("Destination Info"), {"fields": ("body_dst", "headers_dst", "params_dst", "response_dst", "url_dst")}),
        ) + self.fieldsets


admin.site.register(Task, TaskAdmin)
