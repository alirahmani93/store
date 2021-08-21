from django.db import models
from product.models import Product


# Create your models here.

class Cart(models.Model):
    status_choices = (    ('on_cart', 'on_cart'), ('ready_to_payed', 'ready_to_payed')     )

    # user_fk = models.ForeignKey("USER", on_delete=models.CASCADE)
    product_fk = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=100, choices=status_choices, default=None)
    count = models.IntegerField(verbose_name="تعداد محصول")

    # if payment_check == "OK" then add to User__score
    score_of_this_cart = models.SmallIntegerField(help_text="امتیاز این سبد خرید را در خودش نگه میداره ")

    def __str__(self):
        return self.product_fk.name
