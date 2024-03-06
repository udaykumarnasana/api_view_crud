# Generated by Django 5.0.2 on 2024-03-06 05:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productcatogory',
            fields=[
                ('pcid', models.IntegerField(primary_key=True, serialize=False)),
                ('pcname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pcname', models.CharField(max_length=100)),
                ('pcprice', models.IntegerField()),
                ('pcbrand', models.CharField(max_length=100)),
                ('pcid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.productcatogory')),
            ],
        ),
    ]
