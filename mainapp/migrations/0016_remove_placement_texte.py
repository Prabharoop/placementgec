# Generated by Django 2.1.2 on 2019-02-18 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_auto_20181126_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placement',
            name='texte',
        ),
    ]
