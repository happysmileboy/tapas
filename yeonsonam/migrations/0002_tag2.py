# Generated by Django 2.0.2 on 2018-02-17 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yeonsonam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
