# Generated by Django 2.1.2 on 2018-11-19 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20181119_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='placement',
            name='choicee',
            field=models.BooleanField(default=True),
        ),
    ]