from rest_framework import routers
from common import viewsets

router = routers.DefaultRouter()
router.register(r"products", viewsets.ProductViewSet, basename="models")
