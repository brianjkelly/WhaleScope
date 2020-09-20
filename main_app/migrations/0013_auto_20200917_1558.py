# Generated by Django 3.1 on 2020-09-17 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20200916_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sighting',
            name='location',
        ),
        migrations.AddField(
            model_name='sighting',
            name='latitude',
            field=models.DecimalField(decimal_places=9, default=34.0259, max_digits=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sighting',
            name='longitude',
            field=models.DecimalField(decimal_places=9, default=-118.7798, max_digits=12),
            preserve_default=False,
        ),
    ]