from django.urls import include, path
from rest_framework import routers

from omni_pro_oms.views import OmsCore, config, operation, operation_type, task, tenant, tenant_operation

router = routers.DefaultRouter()

router.register(r"tenants", tenant.TenantViewSet)
router.register(r"operations", operation.OperationViewSet)
router.register(r"tasks", task.TaskViewSet)
router.register(r"configs", config.ConfigViewSet)
router.register(r"operation_types", operation_type.OperationTypeViewSet)
router.register(r"tenant_operations", tenant_operation.TenantOperationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("receipt/stock", OmsCore.as_view({"post": "receipt_stock"}), name="receipt-stock"),
]
