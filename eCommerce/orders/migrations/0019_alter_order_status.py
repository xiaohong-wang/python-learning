# Generated by Django 4.1 on 2022-10-11 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('refund', 'Refund'), ('paid', 'Paid'), ('delivered', 'Delivered'), ('shipped', 'Shipped'), ('created', 'Created')], default='created', max_length=20),
        ),
    ]
