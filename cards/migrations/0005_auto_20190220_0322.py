# Generated by Django 2.1.5 on 2019-02-19 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_auto_20190220_0302'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurecard',
            name='useless',
            field=models.CharField(blank=True, default='', max_length=1),
        ),
        migrations.AddField(
            model_name='shieldcard',
            name='useless',
            field=models.CharField(blank=True, default='', max_length=1),
        ),
    ]