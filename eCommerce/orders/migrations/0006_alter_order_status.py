# Generated by Django 4.1 on 2022-10-06 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_managers_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('delivered', 'Delivered'), ('shipped', 'Shipped'), ('paid', 'Paid'), ('created', 'Created'), ('refund', 'Refund')], default='created', max_length=20),
        ),
    ]
