# Generated by Django 4.0.1 on 2022-01-31 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauthentication', '0003_auto_20220122_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]