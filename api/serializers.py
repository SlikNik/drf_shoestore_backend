from rest_framework import serializers
from manufacturer.models import Manufacturer
from shoe.models import Shoe, ShoeColor, ShoeType

class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['name', 'website']


class ShoeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shoe
        fields = ['size', 'brand_name', 'manufacturer', 'color', 'material', 'shoe_type', 'fasten_type']

class ShoeTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoeType
        fields = ['style']

class ShoeColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ['color_name']


# Joe grow up in the African Savanna as a monkey watcher all his time there.
