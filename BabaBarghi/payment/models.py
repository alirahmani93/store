from django.db import models

from json import loads , dumps

from cart.models import Cart
# from shiping.models import Shiping
# Create your models here.


class Payment(models.Model):
    cart_fk = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    # shiping = models.ForeignKey("Shiping", on_delete=models.CASCADE, null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.cart_fk} , {self.status}"