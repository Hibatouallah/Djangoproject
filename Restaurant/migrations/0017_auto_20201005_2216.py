# Generated by Django 2.2.14 on 2020-10-05 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0016_auto_20201005_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='menu',
            field=models.ImageField(default='menu_pics/defaultrestau.png', upload_to='restau_pics'),
        ),
    ]
