# Generated by Django 2.1.4 on 2019-01-13 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_wisdomcard_special'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('pic', models.ImageField(upload_to='')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('special', models.CharField(choices=[('immed', '非延时'), ('delay', '延时'), ('ruse', '诡计'), ('power', '势力')], default='immed', max_length=20)),
                ('point', models.CharField(max_length=5)),
                ('pattern', models.CharField(choices=[('heart', '红桃'), ('spade', '黑桃'), ('diamond', '方块'), ('club', '梅花')], max_length=10)),
                ('effect', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
