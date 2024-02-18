from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.db import models
from django.utils.translation import gettext_lazy as _
from omni_pro_base.models import OmniModel


class Operation(OmniModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    destination = models.CharField(max_length=255, verbose_name=_("Destination"))
    score = models.IntegerField(verbose_name="Score")
    endpoint_url = models.CharField(max_length=255, verbose_name=_("Endpoint URL"))
    http_method = models.CharField(max_length=255, verbose_name=_("HTTP Method"))
    timeout = models.IntegerField(verbose_name=_("Timeout"))
    auth_type = models.CharField(max_length=255, verbose_name=_("Auth Type"))
    headers = models.JSONField(verbose_name=_("Headers"), blank=True, null=True)

    history = AuditlogHistoryField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Operation")
        verbose_name_plural = _("Operations")


auditlog.register(Operation)
