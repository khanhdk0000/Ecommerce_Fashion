from django.db import models

from checkout.models import RegisteredCustomer


class Favorite(models.Model):
    favorite_id = models.AutoField(primary_key=True, null=False, unique=True, auto_created=True)
    customer = models.ForeignKey(
        RegisteredCustomer,
        null=False,
        on_delete=models.CASCADE,
        related_name="customer_favorite",
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'favorite'
