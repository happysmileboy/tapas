# Generated by Django 2.0.2 on 2018-02-09 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20, verbose_name='닉네임')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile/%Y/%m/%d/')),
                ('birth_day', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('phone_number', models.IntegerField(blank=True)),
                ('address', models.TextField(blank=True)),
                ('email_address', models.EmailField(blank=True, max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('gender', models.CharField(choices=[('M', 'Homme'), ('F', 'Femme')], max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
