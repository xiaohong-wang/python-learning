# Generated by Django 4.1 on 2022-10-12 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0027_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('refund', 'Refund'), ('shipped', 'Shipped'), ('created', 'Created'), ('paid', 'Paid'), ('delivered', 'Delivered')], default='created', max_length=20),
        ),
    ]
