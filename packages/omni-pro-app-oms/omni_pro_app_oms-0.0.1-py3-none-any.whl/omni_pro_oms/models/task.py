from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.db import models
from django.utils.translation import gettext_lazy as _
from omni_pro_base.models import OmniModel

from .operation import Operation
from .tenant import Tenant

STATUS_CHOICES = (
    ("waiting", "Waiting"),
    ("error", "Error"),
    ("success", "Success"),
)


class Task(OmniModel):
    name = models.CharField(max_length=256, verbose_name=_("Name"))
    tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE, verbose_name=_("Tenant"), related_name="tasks")
    operation_id = models.ForeignKey(
        Operation, on_delete=models.CASCADE, verbose_name=_("Operation"), related_name="tasks"
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=256, default="waiting", verbose_name=_("Status"))
    body_src = models.JSONField(verbose_name=_("Body Source"))
    headers_src = models.JSONField(verbose_name=_("Headers Source"))
    params_src = models.JSONField(verbose_name=_("Params Source"))
    response_src = models.JSONField(verbose_name=_("Response Source"))
    url_src = models.CharField(max_length=256, verbose_name=_("URL Source"))
    body_dst = models.JSONField(verbose_name=_("Body Destination"))
    headers_dst = models.JSONField(verbose_name=_("Headers Destination"))
    params_dst = models.JSONField(verbose_name=_("Params Destination"))
    response_dst = models.JSONField(verbose_name=_("Response Destination"))
    url_dst = models.CharField(max_length=256, verbose_name=_("URL Destination"))
    time = models.IntegerField(verbose_name=_("Time (ms)"))

    history = AuditlogHistoryField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")


auditlog.register(Task)
