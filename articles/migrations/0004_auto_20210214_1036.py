# Generated by Django 3.1.4 on 2021-02-14 05:06

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20210202_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
