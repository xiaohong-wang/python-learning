# Generated by Django 4.1 on 2022-10-12 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0026_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('shipped', 'Shipped'), ('delivered', 'Delivered'), ('paid', 'Paid'), ('created', 'Created'), ('refund', 'Refund')], default='created', max_length=20),
        ),
    ]
