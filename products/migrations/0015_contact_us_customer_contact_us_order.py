# Generated by Django 4.2.16 on 2024-12-07 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_contact_us'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_us',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.customer'),
        ),
        migrations.AddField(
            model_name='contact_us',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.order'),
        ),
    ]
