from rest_framework import serializers
from checkout.models import Order, OrderDetail, RegisteredCustomer
from product.models import Product
from product.serializers import ProductSerializer


class RegisteredCustomerSerializer(serializers.ModelSerializer):
    customer_id = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = RegisteredCustomer
        fields = ("customer_id", "name", "email")

    def create(self, validated_data):
        return RegisteredCustomer.objects.create(
            **validated_data
        )

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.email = validated_data.get("email", instance.email)

        instance.save()
        return instance


class OrderSerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField(required=False)
    required_date = serializers.DateTimeField(required=True)
    ordered_date = serializers.DateTimeField(required=True)
    customer = RegisteredCustomerSerializer()

    class Meta:
        model = Order
        fields = ("order_id", "required_date",
                  "ordered_date", "customer")

    def create(self, validated_data):
        customer = validated_data.get("customer")
        # print("-" * 50, end="\n\n")
        # print(customer, end="\n\n")
        # print(dir(customer))
        # print("-" * 50, end="\n\n")
        customer_instance, _ = RegisteredCustomer.objects.get_or_create(
            **customer
        )

        return Order.objects.create(
            required_date=validated_data.get("required_date"),
            ordered_date=validated_data.get("ordered_date"),
            customer=customer_instance,
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
    order = OrderSerializer(required=False)
    product = ProductSerializer(required=False)
    quantity = serializers.IntegerField(required=True)
    price = serializers.DecimalField(
        required=True, decimal_places=2, max_digits=10)

    class Meta:
        model = OrderDetail
        fields = ("order", "product", "quantity", "price")

    def create(self, validated_data):
        order = validated_data.get('order')
        # print("-" * 50, end="\n\n")
        # print(order, end="\n\n")
        # print(type(order))
        # print(dir(order))
        # print("-" * 50, end="\n\n")
        customer = order.get('customer')
        customer_instance, _ = RegisteredCustomer.objects.get_or_create(
            **customer
        )
        order_instance, _ = Order.objects.get_or_create(
            order_id=order.get('order_id'),
            required_date=order.get('required_date'),
            ordered_date=order.get('ordered_date'),
            customer=customer_instance
        )

        product = validated_data.get('product')
        product_instance, _ = Product.objects.get_or_create(
            **product
        )

        return OrderDetail.objects.create(
            order=order_instance,
            product=product_instance,
            quantity=validated_data.get("quantity"),
            price=validated_data.get("price"),
        )

    def update(self, instance, validated_data):
        print("-" * 50, end="\n\n")
        print(validated_data, end="\n\n")
        print("-" * 50, end="\n\n")
        instance.quantity = validated_data.get("quantity", instance.quantity)
        instance.price = validated_data.get("price", instance.price)

        instance.save()
        return instance
