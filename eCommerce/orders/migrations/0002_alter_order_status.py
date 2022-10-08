# Generated by Django 4.1 on 2022-10-04 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('shipped', 'Shipped'), ('refund', 'Refund'), ('created', 'Created'), ('paid', 'Paid'), ('delivered', 'Delivered')], default='created', max_length=20),
        ),
    ]
