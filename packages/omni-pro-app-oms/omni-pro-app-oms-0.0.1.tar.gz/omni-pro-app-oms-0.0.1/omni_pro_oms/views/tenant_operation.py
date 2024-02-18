from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import viewsets

from omni_pro_oms.models import TenantOperation
from omni_pro_oms.serializers import TenantOperationSerializer


class TenantOperationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows configs to be viewed or edited.
    """

    queryset = TenantOperation.objects.all()
    serializer_class = TenantOperationSerializer
    permission_classes = [TokenHasReadWriteScope]
