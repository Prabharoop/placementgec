# Generated by Django 2.1.2 on 2018-11-10 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20181110_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placement',
            name='univname',
            field=models.CharField(max_length=100, null=True, verbose_name='University Name'),
        ),
    ]
