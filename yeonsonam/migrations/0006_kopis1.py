# Generated by Django 2.0.2 on 2018-02-03 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yeonsonam', '0005_auto_20180203_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kopis1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.TextField(blank=True, null=True)),
                ('field2', models.TextField(blank=True, null=True)),
                ('field3', models.TextField(blank=True, null=True)),
                ('field4', models.TextField(blank=True, null=True)),
                ('field5', models.TextField(blank=True, null=True)),
                ('field6', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'kopis1',
                'managed': False,
            },
        ),
    ]
