# Generated by Django 2.2.14 on 2020-10-02 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0002_restaurant_totallikes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentaire',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='totallikes',
        ),
        migrations.AddField(
            model_name='commentaire',
            name='totallikes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='totallikes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
