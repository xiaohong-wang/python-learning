# Generated by Django 4.1 on 2022-10-07 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('refund', 'Refund'), ('delivered', 'Delivered'), ('paid', 'Paid'), ('shipped', 'Shipped')], default='created', max_length=20),
        ),
    ]
