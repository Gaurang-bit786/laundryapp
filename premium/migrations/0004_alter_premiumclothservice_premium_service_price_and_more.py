# Generated by Django 4.0.1 on 2022-02-25 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premium', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premiumclothservice',
            name='premium_service_price',
            field=models.CharField(default=0, max_length=150),
        ),
        migrations.AlterField(
            model_name='premiumclothservice',
            name='service',
            field=models.IntegerField(default=0),
        ),
    ]