# Generated by Django 2.2 on 2020-03-07 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200307_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='RegNo',
            field=models.CharField(default='First Year', max_length=9),
        ),
    ]
