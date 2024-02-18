from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import viewsets

from omni_pro_oms.models import Config
from omni_pro_oms.serializers import ConfigSerializer


class ConfigViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows configs to be viewed or edited.
    """

    queryset = Config.objects.all()
    serializer_class = ConfigSerializer
    permission_classes = [TokenHasReadWriteScope]
