# Generated by Django 4.1 on 2022-10-04 22:02

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_status'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='order',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('refund', 'Refund'), ('paid', 'Paid')], default='created', max_length=20),
        ),
    ]
