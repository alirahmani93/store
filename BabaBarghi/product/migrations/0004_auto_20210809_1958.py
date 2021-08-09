# Generated by Django 3.2.6 on 2021-08-09 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_price_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='picture',
        ),
        migrations.AlterField(
            model_name='price',
            name='date_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='date_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='set_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='unstable_price',
            field=models.FloatField(blank=True, null=True, verbose_name='درصد تخفیف'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='upc',
            field=models.PositiveBigIntegerField(help_text='بارکد ۱۲ رقمی'),
        ),
    ]
