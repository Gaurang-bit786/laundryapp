# Generated by Django 3.1.7 on 2022-02-16 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0026_auto_20220217_0238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderssummary',
            old_name='instrution',
            new_name='instruction',
        ),
    ]
