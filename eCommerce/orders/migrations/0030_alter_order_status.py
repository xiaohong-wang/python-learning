# Generated by Django 4.1 on 2022-10-14 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0029_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('refund', 'Refund'), ('delivered', 'Delivered'), ('paid', 'Paid'), ('created', 'Created'), ('shipped', 'Shipped')], default='created', max_length=20),
        ),
    ]
