from django.db import models

from product.models import Product

# Create your models here.


class RegisteredCustomer(models.Model):
    customer_id = models.AutoField(
        primary_key=True, null=False, unique=True, auto_created=True
    )
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "registered_customer"


class Order(models.Model):
    order_id = models.AutoField(
        primary_key=True, null=False, unique=True, auto_created=True
    )
    required_date = models.DateTimeField(null=False)
    ordered_date = models.DateTimeField(null=False)
    customer = models.ForeignKey(
        RegisteredCustomer,
        null=False,
        on_delete=models.CASCADE,
        related_name="customer_order",
    )

    def __str__(self):
        return f"order_id: {self.order_id}, customer_id: {self.customer}"

    class Meta:
        db_table = "order"


class OrderDetail(models.Model):
    order = models.ForeignKey(
        Order, null=False, on_delete=models.CASCADE, related_name="order_order_detail"
    )
    product = models.ForeignKey(
        Product,
        null=False,
        on_delete=models.CASCADE,
        related_name="product_order_detail",
    )
    quantity = models.IntegerField(null=False, editable=True)
    price = models.DecimalField(null=False, decimal_places=2, max_digits=10)

    def __str__(self):
        return f"order_id: {self.order_id}, product_id: {self.product_id}"

    class Meta:
        db_table = "order_detail"
        unique_together = (("order", "product"),)
