from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    vip = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'discount',
            'test_field',
            'vip',
        ]

    def get_vip(self, obj):
        print(obj.price)
        return obj.test_field()
