# Generated by Django 2.2 on 2020-03-07 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190326_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='YearofStudy',
            field=models.CharField(choices=[('First', 'First Year'), ('Second', 'Second Year'), ('Third', 'Third Year'), ('Fourth', 'Fourth Year'), ('M1st', 'M.Tech First Year'), ('M2nd', 'M.Tech Second Year'), ('phd', 'PHD')], default='', max_length=20),
        ),
    ]
