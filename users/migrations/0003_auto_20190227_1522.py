# Generated by Django 2.1.4 on 2019-02-27 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190216_1025'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userinfo',
            unique_together={('name',)},
        ),
    ]
