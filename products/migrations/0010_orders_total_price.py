# Generated by Django 4.0.1 on 2022-02-22 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_rename_order_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='total_price',
            field=models.IntegerField(null=True),
        ),
    ]
