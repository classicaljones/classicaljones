# Generated by Django 5.1.1 on 2024-11-15 23:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_order_transaction_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavouriteItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderItem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.orderitem')),
            ],
        ),
    ]