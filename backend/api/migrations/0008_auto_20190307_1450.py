# Generated by Django 2.1.7 on 2019-03-07 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_shortprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortprofile',
            name='avatar',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shortprofile',
            name='avatar_full',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shortprofile',
            name='avatar_med',
            field=models.URLField(blank=True, null=True),
        ),
    ]
