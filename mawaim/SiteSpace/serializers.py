from rest_framework import serializers

from SiteSpace.models import Product, Category, Variant


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Category
        fields = ('id', 'category_name')
        read_only_fields = ('id',)


class VariantSerializer(serializers.ModelSerializer):
    """Serializer for ingredient objects"""

    class Variant:
        model = Variant
        fields = ('id', 'variant_name')
        read_only_fields = ('id',)


class ProductSerializer(serializers.ModelSerializer):
    """Serialize a recipe"""
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )
    variant = serializers.PrimaryKeyRelatedField(
        queryset=Variant.objects.all()
    )

    class Meta:
        model = Product
        fields = (
            'id', 'categories', 'name', 'description', 'variants',
            'price', 'count'
        )
        read_only_fields = ('id',)
