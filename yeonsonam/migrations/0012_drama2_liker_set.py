# Generated by Django 2.0.2 on 2018-02-05 20:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yeonsonam', '0011_auto_20180204_0408'),
    ]

    operations = [
        migrations.AddField(
            model_name='drama2',
            name='liker_set',
            field=models.ManyToManyField(related_name='liked_drama2_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
