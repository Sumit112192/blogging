# Generated by Django 2.1 on 2021-02-14 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210214_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
    ]
