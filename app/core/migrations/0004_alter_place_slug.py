# Generated by Django 4.0.2 on 2022-03-02 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_place_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
