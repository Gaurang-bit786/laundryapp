# Generated by Django 3.1.7 on 2022-02-25 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premium', '0009_alter_premiumclothservice_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='premiumclothservice',
            old_name='premium_service_price',
            new_name='premium_services_price',
        ),
        migrations.AlterField(
            model_name='premiumclothcategory',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='premiumclothname',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='premiumclothservice',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='premiumorderssummary',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
