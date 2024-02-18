from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.db import models
from django.utils.translation import gettext_lazy as _
from omni_pro_base.models import OmniModel


class Tenant(OmniModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.CharField(max_length=255, verbose_name=_("Description"))
    code = models.CharField(max_length=255, verbose_name=_("Code"), unique=True)
    client_id = models.CharField(max_length=255, verbose_name=_("Client ID"))
    client_secret = models.CharField(max_length=255, verbose_name=_("Client Secret"))

    history = AuditlogHistoryField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Tenant")
        verbose_name_plural = _("Tenants")


auditlog.register(Tenant)
