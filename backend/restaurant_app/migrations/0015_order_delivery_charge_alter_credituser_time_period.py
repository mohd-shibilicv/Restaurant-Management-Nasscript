# Generated by Django 5.1 on 2024-08-24 15:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0014_order_customer_name_order_customer_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_charge',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='credituser',
            name='time_period',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 23, 15, 11, 56, 240747, tzinfo=datetime.timezone.utc)),
        ),
    ]
