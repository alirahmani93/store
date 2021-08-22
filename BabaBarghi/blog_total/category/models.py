from django.db import models

from lib.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=16, verbose_name='name')
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'category'

    def __str__(self):
        return self.name
