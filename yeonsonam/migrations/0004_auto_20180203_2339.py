# Generated by Django 2.0.2 on 2018-02-03 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yeonsonam', '0003_auto_20180203_2338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drama2',
            old_name='field_dbs',
            new_name='place',
        ),
    ]
