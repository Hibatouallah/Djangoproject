# Generated by Django 2.2.14 on 2020-10-02 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_auto_20201002_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comptegratuit',
            name='photoprofil',
        ),
    ]