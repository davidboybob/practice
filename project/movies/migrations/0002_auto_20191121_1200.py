# Generated by Django 2.2.7 on 2019-11-21 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ('-pk',)},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('-pk',)},
        ),
    ]
