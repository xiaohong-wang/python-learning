# Generated by Django 4.1 on 2022-10-20 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0041_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('paid', 'Paid'), ('delivered', 'Delivered'), ('shipped', 'Shipped'), ('created', 'Created'), ('refund', 'Refund')], default='created', max_length=20),
        ),
    ]