# Generated by Django 2.1.5 on 2019-02-17 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='topic',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
