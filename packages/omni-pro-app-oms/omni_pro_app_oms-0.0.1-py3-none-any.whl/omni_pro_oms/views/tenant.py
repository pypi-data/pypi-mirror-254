from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import viewsets

from omni_pro_oms.models import Tenant
from omni_pro_oms.serializers import TenantSerializer


class TenantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows configs to be viewed or edited.
    """

    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [TokenHasReadWriteScope]
