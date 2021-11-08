from rest_framework import serializers
from .models import Favorite, Contains

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = (
            'favorite_id',
            'customer'
        )

class ContainsSerializer(serializers.ModelSerializer):
    favorite_id = serializers.IntegerField(required=True)
    product_id = serializers.IntegerField(required=True)

    class Meta:
        model = Contains
        fields = (
            'favorite_id',
            'product_id'
        )

    def create(self, validated_data):
        return Contains.objects.create(
            favorite_id=validated_data.get("favorite_id"),
            product_id=validated_data.get("product_id"),
        )

    # def update(self, instance, validated_data):
    #     instance.quantity = validated_data.get("quantity", instance.quantity)
    #     instance.price = validated_data.get("price", instance.price)

    #     instance.save()
    #     return instance

