# Generated by Django 3.1.1 on 2020-09-15 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20200915_0457'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='replies',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.comment'),
        ),
    ]
