# Generated by Django 2.2.6 on 2019-11-02 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0010_auto_20191102_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rescue_entry',
            name='lat_position',
            field=models.FloatField(default=None),
        ),
    ]
