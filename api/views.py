from manufacturer.models import Manufacturer
from shoe.models import Shoe, ShoeColor, ShoeType
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import ManufacturerSerializer, ShoeSerializer, ShoeTypeSerializer, ShoeColorSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows manufacturers to be viewed or edited.
    """
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer



class ShoeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows shoes to be viewed or edited.
    """
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer



class ShoeTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows shoe types to be viewed or edited.
    """
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer


class ShoeColorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows shoe colors to be viewed or edited.
    """
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer


