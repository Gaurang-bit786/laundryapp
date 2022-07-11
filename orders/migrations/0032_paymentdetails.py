# Generated by Django 3.1.7 on 2022-02-16 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0031_auto_20220217_0308'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('cloth_name', models.CharField(max_length=150)),
                ('price', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=250)),
                ('quantity', models.CharField(max_length=150)),
                ('ironing', models.BooleanField(default=False)),
                ('hot_water', models.BooleanField(default=False)),
                ('cold_water', models.BooleanField(default=False)),
                ('washing_liquid', models.BooleanField(default=False)),
                ('softern', models.BooleanField(default=False)),
                ('pick_up_date', models.DateField()),
                ('delivery', models.DateField()),
            ],
        ),
    ]
