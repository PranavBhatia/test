# Generated by Django 4.2.6 on 2023-11-08 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
                ('coverImage', models.TextField()),
                ('numPages', models.IntegerField()),
                ('desctipion', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
