from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import viewsets

from omni_pro_oms.models import OperationType
from omni_pro_oms.serializers import OperationTypeSerializer


class OperationTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows configs to be viewed or edited.
    """

    queryset = OperationType.objects.all()
    serializer_class = OperationTypeSerializer
    permission_classes = [TokenHasReadWriteScope]
