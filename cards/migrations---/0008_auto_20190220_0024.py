# Generated by Django 2.1.5 on 2019-02-19 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0007_auto_20190220_0015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='badcard',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='basiccard',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='equipcard',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='herocard',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='wisdomcard',
            name='pub_date',
        ),
    ]
