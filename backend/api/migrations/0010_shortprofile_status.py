# Generated by Django 2.1.7 on 2019-03-07 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_shortprofile_steam_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortprofile',
            name='status',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
