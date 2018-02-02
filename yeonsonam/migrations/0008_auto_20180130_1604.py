# Generated by Django 2.0.1 on 2018-01-30 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yeonsonam', '0007_auto_20180130_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drama',
            name='sequence',
        ),
        migrations.AddField(
            model_name='drama',
            name='sequence',
            field=models.ManyToManyField(to='yeonsonam.Sequence'),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='sequence_time',
            field=models.TimeField(),
        ),
    ]
