# Generated by Django 4.2.16 on 2024-12-01 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_shippingaddress_email_shippingaddress_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=700, null=True),
        ),
    ]