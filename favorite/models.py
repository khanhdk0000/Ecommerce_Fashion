from django.db import models

from checkout.models import RegisteredCustomer
from product.models import Product
from django.db.models import Deferrable, UniqueConstraint


class Favorite(models.Model):
    favorite_id = models.AutoField(
        primary_key=True, null=False, unique=True, auto_created=True)
    customer = models.ForeignKey(
        RegisteredCustomer,
        null=False,
        on_delete=models.CASCADE,
        related_name="customer_favorite",
    )

    def __str__(self):
        return f"favorite_id: {self.favorite_id}, customer_id: {self.customer.customer_id}"

    class Meta:
        db_table = 'favorite'


class Contains(models.Model):
    favorite = models.ForeignKey(
        Favorite, null=False, on_delete=models.CASCADE, related_name="favorite_contains"
    )
    product = models.ForeignKey(
        Product,
        null=False,
        on_delete=models.CASCADE,
        related_name="product_contains",
    )

    def __str__(self):
        return f"{self.product.product_id}"

    class Meta:
        db_table = "contains"
        # unique_together = (("favorite", "product"),)
        constraints = [
            models.UniqueConstraint(
                fields=['favorite', 'product'], name='unique')
        ]
