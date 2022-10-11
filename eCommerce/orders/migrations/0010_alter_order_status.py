# Generated by Django 4.1 on 2022-10-07 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_order_billing_profile_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('shipped', 'Shipped'), ('paid', 'Paid'), ('created', 'Created'), ('delivered', 'Delivered'), ('refund', 'Refund')], default='created', max_length=20),
        ),
    ]