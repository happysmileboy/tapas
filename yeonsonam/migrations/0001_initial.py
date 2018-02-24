# Generated by Django 2.0.2 on 2018-02-23 23:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.TextField(blank=True, null=True)),
                ('field2', models.TextField(blank=True, null=True)),
                ('field3', models.TextField(blank=True, null=True)),
                ('field4', models.TextField(blank=True, null=True)),
                ('field5', models.TextField(blank=True, null=True)),
                ('field6', models.TextField(blank=True, null=True)),
                ('field7', models.TextField(blank=True, null=True)),
                ('field8', models.TextField(blank=True, null=True)),
                ('field9', models.TextField(blank=True, null=True)),
                ('field11', models.TextField(blank=True, null=True)),
                ('field12', models.TextField(blank=True, null=True)),
                ('field13', models.TextField(blank=True, null=True)),
                ('field14', models.TextField(blank=True, null=True)),
                ('field15', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'place_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Drama2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.TextField(blank=True, null=True)),
                ('perf_kind', models.TextField(blank=True, null=True)),
                ('perf_id', models.TextField(blank=True, null=True)),
                ('openrun', models.TextField(blank=True, null=True)),
                ('poster', models.TextField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('end_date', models.TextField(blank=True, null=True)),
                ('perf_state', models.TextField(blank=True, null=True)),
                ('detail_url', models.TextField(blank=True, null=True)),
                ('age', models.TextField(blank=True, null=True)),
                ('casts', models.TextField(blank=True, null=True)),
                ('crews', models.TextField(blank=True, null=True)),
                ('theater_company', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Drama2',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='drama',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yeonsonam.Drama2'),
        ),
    ]
