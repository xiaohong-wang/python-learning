# Generated by Django 4.1 on 2022-10-20 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_remove_cart_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='items_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]