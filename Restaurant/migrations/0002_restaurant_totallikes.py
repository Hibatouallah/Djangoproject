# Generated by Django 2.2.14 on 2020-10-02 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='totallikes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
