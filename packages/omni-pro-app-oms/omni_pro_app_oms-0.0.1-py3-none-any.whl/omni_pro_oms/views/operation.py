from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import viewsets

from omni_pro_oms.models import Operation
from omni_pro_oms.serializers import OperationSerializer


class OperationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows configs to be viewed or edited.
    """

    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    permission_classes = [TokenHasReadWriteScope]
