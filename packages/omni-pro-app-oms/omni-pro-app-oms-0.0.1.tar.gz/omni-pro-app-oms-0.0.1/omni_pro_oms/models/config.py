from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.db import models
from django.utils.translation import gettext_lazy as _
from omni_pro_base.models import OmniModel


class Config(OmniModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    base_url = models.CharField(max_length=255, verbose_name=_("Base URL"))
    auth = models.JSONField(verbose_name=_("Auth"), blank=True, null=True)
    token = models.JSONField(verbose_name=_("Token"), blank=True, null=True)

    history = AuditlogHistoryField()

    def __str__(self):
        return self.base_url

    class Meta:
        verbose_name = _("Configuration")
        verbose_name_plural = _("Configurations")
        # ordering = ['created_at']


auditlog.register(Config)
