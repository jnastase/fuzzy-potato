from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from common.models import Product
from common.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
