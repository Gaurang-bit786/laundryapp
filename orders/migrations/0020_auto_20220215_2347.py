# Generated by Django 3.1.7 on 2022-02-15 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_auto_20220215_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderssummary',
            name='cloth_image',
            field=models.ImageField(null=True, upload_to='media/cloth/%Y/%m/%d/'),
        ),
    ]
