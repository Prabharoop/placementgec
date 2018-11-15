# Generated by Django 2.1.2 on 2018-11-15 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20181111_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='placement',
            name='gender',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Others')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='placement',
            name='reg',
            field=models.CharField(max_length=50, null=True, verbose_name='Registration Number'),
        ),
    ]
