# Generated by Django 4.1 on 2022-10-06 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('delivered', 'Delivered'), ('created', 'Created'), ('refund', 'Refund'), ('paid', 'Paid'), ('shipped', 'Shipped')], default='created', max_length=20),
        ),
    ]
