# Generated by Django 3.1.7 on 2022-02-15 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_clothname_orderssummary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderssummary',
            name='delivery_date',
            field=models.DateTimeField(null=True),
        ),
    ]
