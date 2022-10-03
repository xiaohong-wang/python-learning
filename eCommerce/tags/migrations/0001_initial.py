# Generated by Django 4.1.1 on 2022-10-01 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_rename_acitve_product_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('acitve', models.BooleanField(default=True)),
                ('product', models.ManyToManyField(blank=True, to='products.product')),
            ],
        ),
    ]