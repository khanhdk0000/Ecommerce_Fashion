from rest_framework import serializers
from checkout.models import Order, OrderDetail, RegisteredCustomer


class RegisteredCustomerSerializer(serializers.ModelSerializer):
    customer_id = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = RegisteredCustomer
        fields = ("customer_id", "name", "email")

    def create(self, validated_data):
        return RegisteredCustomer.objects.create(
            customer_id=validated_data.get("customer_id"),
            name=validated_data.get("name"),
            email=validated_data.get("email"),
        )

    def update(self, instance, validated_data):
        instance.customer_id = validated_data.get("customer_id", instance.name)
        instance.name = validated_data.get("name", instance.name)
        instance.email = validated_data.get("email", instance.email)

        instance.save()
        return instance


class OrderSerializer(serializers.ModelSerializer):
    required_date = serializers.DateTimeField(required=True)
    ordered_date = serializers.DateTimeField(required=True)

    class Meta:
        model = Order
        fields = ("order_id", "required_date", "ordered_date", "customer_id")

    def create(self, validated_data):
        return Order.objects.create(
            required_date=validated_data.get("required_date"),
            ordered_date=validated_data.get("ordered_date"),
            customer_id=self.context["customer_id"],
        )

    def update(self, instance, validated_data):
        instance.required_date = validated_data.get(
            "required_date", instance.required_date
        )
        instance.ordered_date = validated_data.get(
            "required_date", instance.ordered_date
        )

        instance.save()
        return instance


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ("order_id", "product_id", "quantity", "price")

    def create(self, validated_data):
        return OrderDetail.objects.create(
            order_id=self.context["order_id"],
            product_id=self.context["product_id"],
            quantity=validated_data.get("quantity"),
            price=validated_data.get("price"),
        )

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get("quantity", instance.quantity)
        instance.price = validated_data.get("price", instance.price)

        instance.save()
        return instance
