# Generated by Django 5.1.1 on 2024-11-16 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_favouriteitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='favouriteitem',
            name='favourite',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]