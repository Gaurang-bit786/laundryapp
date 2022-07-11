# Generated by Django 3.1.7 on 2022-02-15 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_clothcategory_clothname_orderssummary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothname',
            name='cloth_category_name',
        ),
        migrations.RemoveField(
            model_name='orderssummary',
            name='cloth_name',
        ),
        migrations.RemoveField(
            model_name='orderssummary',
            name='user',
        ),
        migrations.DeleteModel(
            name='ClothCategory',
        ),
        migrations.DeleteModel(
            name='ClothName',
        ),
        migrations.DeleteModel(
            name='OrdersSummary',
        ),
    ]