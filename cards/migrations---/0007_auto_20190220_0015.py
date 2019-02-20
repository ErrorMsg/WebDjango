# Generated by Django 2.1.5 on 2019-02-19 16:15

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_auto_20190219_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horsecard',
            name='effect',
        ),
        migrations.RemoveField(
            model_name='horsecard',
            name='pattern',
        ),
        migrations.RemoveField(
            model_name='horsecard',
            name='point',
        ),
        migrations.RemoveField(
            model_name='measurecard',
            name='effect',
        ),
        migrations.RemoveField(
            model_name='measurecard',
            name='pattern',
        ),
        migrations.RemoveField(
            model_name='measurecard',
            name='point',
        ),
        migrations.RemoveField(
            model_name='shieldcard',
            name='effect',
        ),
        migrations.RemoveField(
            model_name='shieldcard',
            name='pattern',
        ),
        migrations.RemoveField(
            model_name='shieldcard',
            name='point',
        ),
        migrations.RemoveField(
            model_name='weaponcard',
            name='effect',
        ),
        migrations.RemoveField(
            model_name='weaponcard',
            name='pattern',
        ),
        migrations.RemoveField(
            model_name='weaponcard',
            name='point',
        ),
        migrations.AddField(
            model_name='horsecard',
            name='equip',
            field=models.ForeignKey(default=datetime.datetime(2019, 2, 19, 16, 14, 55, 972618, tzinfo=utc), on_delete=django.db.models.deletion.CASCADE, to='cards.EquipCard'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='measurecard',
            name='equip',
            field=models.ForeignKey(default=datetime.datetime(2019, 2, 19, 16, 15, 5, 349349, tzinfo=utc), on_delete=django.db.models.deletion.CASCADE, to='cards.EquipCard'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shieldcard',
            name='equip',
            field=models.ForeignKey(default=datetime.datetime(2019, 2, 19, 16, 15, 10, 867769, tzinfo=utc), on_delete=django.db.models.deletion.CASCADE, to='cards.EquipCard'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weaponcard',
            name='equip',
            field=models.ForeignKey(default=datetime.datetime(2019, 2, 19, 16, 15, 16, 40892, tzinfo=utc), on_delete=django.db.models.deletion.CASCADE, to='cards.EquipCard'),
            preserve_default=False,
        ),
    ]