# Generated by Django 3.2.3 on 2022-03-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premium', '0018_premiumorderssummary_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premiumorderssummary',
            name='address',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
