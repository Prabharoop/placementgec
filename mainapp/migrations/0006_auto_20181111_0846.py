# Generated by Django 2.1.2 on 2018-11-11 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20181110_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='placement',
            name='custatus',
            field=models.CharField(choices=[('comp', 'Completed'), ('purs', 'Pursuing'), ('noto', 'Not Opted')], max_length=50, null=True, verbose_name='Current Status'),
        ),
        migrations.AddField(
            model_name='placement',
            name='degree',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='placement',
            name='domain',
            field=models.CharField(choices=[('me', 'Mechanical'), ('cse', 'Computer Science & IT'), ('ece', 'Electronics And Communication'), ('eee', 'Electrical And Electronics'), ('oth', 'Others')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='placement',
            name='univname',
            field=models.CharField(max_length=100, null=True, verbose_name='University Name'),
        ),
    ]
