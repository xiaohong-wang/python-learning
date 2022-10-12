# Generated by Django 4.1 on 2022-10-11 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0023_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('refund', 'Refund'), ('created', 'Created'), ('shipped', 'Shipped'), ('paid', 'Paid'), ('delivered', 'Delivered')], default='created', max_length=20),
        ),
    ]
