# Generated by Django 3.1.4 on 2021-01-16 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouseApi', '0007_auto_20210116_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse_description',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
