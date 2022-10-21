# Generated by Django 4.1 on 2022-10-18 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0037_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('paid', 'Paid'), ('created', 'Created'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('refund', 'Refund')], default='created', max_length=20),
        ),
    ]