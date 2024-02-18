from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.db import models
from django.utils.translation import gettext_lazy as _
from omni_pro_base.models import OmniModel


class OperationType(OmniModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    code = models.CharField(max_length=255, verbose_name=_("Code"), unique=True)

    history = AuditlogHistoryField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Operation Type")
        verbose_name_plural = _("Operation Types")


auditlog.register(OperationType)
