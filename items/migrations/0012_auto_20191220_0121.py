# Generated by Django 2.2.7 on 2019-12-20 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0011_auto_20191218_0051'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={},
        ),
        migrations.RemoveIndex(
            model_name='item',
            name='id_index',
        ),
    ]
