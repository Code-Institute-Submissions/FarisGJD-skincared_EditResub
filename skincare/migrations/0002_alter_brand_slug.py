# Generated by Django 3.2 on 2022-10-03 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skincare', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.SlugField(max_length=200, null=True),
        ),
    ]
