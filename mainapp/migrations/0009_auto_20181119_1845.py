# Generated by Django 2.1.2 on 2018-11-19 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20181117_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='placement',
            name='choicea',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='placement',
            name='choiceb',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='placement',
            name='choicec',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='placement',
            name='choiced',
            field=models.BooleanField(null=True),
        ),
    ]
