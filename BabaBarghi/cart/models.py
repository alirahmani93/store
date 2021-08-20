from django.db import models
from product.models import Product


# Create your models here.

class Cart(models.Model):
    count = models.IntegerField(verbose_name="تعداد محصول")
    user_fk = None
    prodct_fk = models.ManytoManyField("Product", on_delete=models.CASCADE)

    # if payment_check == "OK" then add to User__score
    score_of_this_cart = models.SmallAutoField(help_text="امتیاز این سبد خرید را در خودش نگه میداره ")
