# Generated by Django 2.2.6 on 2019-11-02 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0009_auto_20191102_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rescue_entry',
            name='long_position',
            field=models.FloatField(default=None),
        ),
    ]
