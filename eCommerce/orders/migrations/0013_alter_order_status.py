# Generated by Django 4.1 on 2022-10-11 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_order_billing_address_order_shipping_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('refund', 'Refund'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('paid', 'Paid')], default='created', max_length=20),
        ),
    ]
