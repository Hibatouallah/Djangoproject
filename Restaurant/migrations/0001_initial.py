# Generated by Django 2.2.14 on 2020-08-24 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Accounts', '0003_auto_20200823_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='categoriemenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=32, verbose_name='menu category name')),
                ('additional_text', models.CharField(blank=True, help_text="The additional text is any bit of related information to go along with a menu category, i.e. the 'Pasta' category might have details that say 'All entrees come with salad and bread'.", max_length=128, null=True)),
                ('order', models.IntegerField(default=0, help_text='The order is the order that this category should appear in when rendered on the templates.')),
            ],
            options={
                'verbose_name': 'menu category',
                'verbose_name_plural': 'menu categories',
                'ordering': ['order', 'intitule'],
            },
        ),
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('intitule', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=9000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('restaurant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Restaurant.Restaurant')),
                ('intitule', models.CharField(max_length=24, unique=True, verbose_name='menu name')),
                ('slug', models.SlugField(help_text='The slug is the URL friendly version of the menu name, so that this can be accessed at a URL like mysite.com/menus/dinner/.', max_length=24, null=True, unique=True)),
                ('description', models.CharField(blank=True, help_text='Any additional text that the menu might need, i.e. Served between 11:00am and 4:00pm.', max_length=128, null=True)),
                ('order', models.PositiveSmallIntegerField(default=0, help_text='The order of the menu determines where this menu appears alongside other menus.')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=20)),
                ('intitule', models.CharField(max_length=200)),
                ('intitule_tag', models.CharField(default='tag', max_length=200)),
                ('website', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('horaire', models.CharField(max_length=20)),
                ('adresse', models.CharField(max_length=1000)),
                ('numtele', models.CharField(max_length=20)),
                ('cuisine', models.ManyToManyField(to='Restaurant.Cuisine', verbose_name='cuisine')),
                ('directeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Comptepayant')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='restau_pics')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurant.Restaurant')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.Comptegratuit')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
                ('prix', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='menu')),
                ('epicee', models.BooleanField(default=False)),
                ('sans_gluten', models.BooleanField(default=False)),
                ('categoriemenu', models.ManyToManyField(to='Restaurant.categoriemenu')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='restau_pics')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Restaurant.Post')),
            ],
        ),
        migrations.AddField(
            model_name='categoriemenu',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurant.Menu'),
        ),
    ]
