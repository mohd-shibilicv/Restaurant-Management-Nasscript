# Generated by Django 5.1 on 2024-08-22 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_drivers', '0003_remove_deliveryorder_order_details_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deliveryorder',
            options={'ordering': ('-updated_at',)},
        ),
    ]
