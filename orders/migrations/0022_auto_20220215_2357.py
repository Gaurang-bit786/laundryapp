# Generated by Django 3.1.7 on 2022-02-15 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0021_auto_20220215_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderssummary',
            name='cloth_image',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
    ]
