# Generated by Django 2.0.2 on 2018-02-03 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yeonsonam', '0004_auto_20180203_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='price',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='price',
            name='site',
        ),
        migrations.RemoveField(
            model_name='drama',
            name='seat_photo',
        ),
        migrations.RemoveField(
            model_name='drama',
            name='sequence',
        ),
        migrations.RemoveField(
            model_name='drama',
            name='Actor',
        ),
        migrations.AddField(
            model_name='drama',
            name='Actor',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='drama',
            name='genre',
        ),
        migrations.AddField(
            model_name='drama',
            name='genre',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='drama',
            name='place',
            field=models.CharField(max_length=150),
        ),
        migrations.RemoveField(
            model_name='drama',
            name='price',
        ),
        migrations.AddField(
            model_name='drama',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Actor',
        ),
        migrations.DeleteModel(
            name='Discount',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Place',
        ),
        migrations.DeleteModel(
            name='Price',
        ),
        migrations.DeleteModel(
            name='Seat_photo',
        ),
        migrations.DeleteModel(
            name='Sequence',
        ),
        migrations.DeleteModel(
            name='Site_reservation',
        ),
    ]