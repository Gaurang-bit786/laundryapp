# Generated by Django 3.2.3 on 2022-04-04 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0039_auto_20220322_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderssummary',
            name='deliver',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderssummary',
            name='pick_up',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderssummary',
            name='working',
            field=models.BooleanField(default=False),
        ),
    ]
