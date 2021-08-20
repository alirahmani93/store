from django.db import models
import datetime

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_image_file_extension, DecimalValidator


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="دسته")
    sub_category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, blank=True,
                                     verbose_name="زیر مجموعه")

    class Meta:
        verbose_name = "دسته بندی ها"
        verbose_name_plural = "گروه بندی"

    def __str__(self):
        return self.title


class Brand(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30, blank=True, null=True, verbose_name="کشور دفتر مرکزی")
    city = models.CharField(max_length=30, blank=True, null=True, verbose_name="شهر دفتر مرکزی")
    phone_number = models.IntegerField(blank=True, null=True, verbose_name="تلفن دفتر مرکزی")
    email = models.EmailField(blank=True, null=True, verbose_name="ایمیل دفتر مرکزی")

    def __str__(self):
        return f"{self.name} , {self.phone_number}, {self.email}, {self.country}, {self.city}"


class Price(models.Model):
    # price_Doller = models.ForeignKey("Product", on_delete=models.SET_NULL, blank=True, null=True)
    # price_Rial = models.ForeignKey("Product", on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey("Product", on_delete=models.CASCADE, blank=True, null=True)
    price = models.FloatField(default=0, help_text="﷼")
    set_time = models.DateTimeField(auto_now_add=True)

    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    Temporary_price = models.FloatField(verbose_name="قیمت مموقت", blank=True, null=True)

    # unstable_price = models.DecimalField(max_digits=2,verbose_name="درصد تخفیف",blank=True, null=True)
    # until = models.DurationField(unstable_price)
    @property
    def original_price(self):
        if datetime.time() > self.date_start and datetime.time() < self.date_end:
            return self.unstable_price
        else:
            return self.price

    def __str__(self):
        return f"{self.product}, {self.price}"


class Picture(models.Model):
    @property
    def validate_path(self):
        """
        A validator is a callable that takes a value and raises a ValidationError if it doesn’t meet some criteria.
         Validators can be useful for re-using validation logic between different types of fields.
        :return: raiseError if it dose not a __path__
        """
        if self is not __path__:
            raise ValidationError(
                _('%(value)s is not a path '),
                params={'value': __path__},
            )

    @property
    def validate_image(self):
        if validate_image_file_extension(self):
            picture = models.ImageField(upload_to="Product",
                                        width_field=100, height_field=160, max_length=100)
            return picture

    picture = models.ImageField(upload_to="Product", max_length=100, null=True, blank=True, default=None)
                                # width_field=100, height_field=160, validators=[validate_path])

    discription = models.CharField(max_length=100,default= None)

    def __str__(self):
        return self.discription


class Product(models.Model):
    name = models.CharField(max_length=50, )
    upc = models.PositiveBigIntegerField(help_text="بارکد ۱۲ رقمی")
    size = models.CharField(max_length=30, null=True, blank=True)
    discription = models.TextField(max_length=30, null=True, blank=True)
    count = models.IntegerField(null=True ,blank=True)
    Not_Exist, Active, Will_not_be_produced, Ordered = "N", "T", "W", "O"
    status_choices = [("N", "Not_Exist"), ("T", "Active"), ("W", "Will_not_be_produced"), ("O", "Ordered")]
    status = models.CharField(choices=status_choices, max_length=1)

    cat = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.ForeignKey("Brand", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name