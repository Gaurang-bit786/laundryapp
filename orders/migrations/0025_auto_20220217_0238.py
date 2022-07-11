# Generated by Django 3.1.7 on 2022-02-16 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0024_auto_20220217_0051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderssummary',
            old_name='order_summary',
            new_name='instrution',
        ),
        migrations.AddField(
            model_name='orderssummary',
            name='paid',
            field=models.BooleanField(default=False, null=True),
        ),
    ]