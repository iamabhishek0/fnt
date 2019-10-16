# Generated by Django 2.2.6 on 2019-10-16 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='rescue_entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('scenario', models.CharField(max_length=1000)),
                ('identification_mark', models.CharField(max_length=100)),
                ('dog_type', models.CharField(max_length=100)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='petition_entry',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]