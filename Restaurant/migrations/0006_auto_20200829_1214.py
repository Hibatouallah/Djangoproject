# Generated by Django 2.2.14 on 2020-08-29 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_auto_20200827_0803'),
        ('Restaurant', '0005_menu_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='likes',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='likes',
            field=models.ManyToManyField(related_name='restaurant', to='Accounts.Comptegratuit'),
        ),
    ]
