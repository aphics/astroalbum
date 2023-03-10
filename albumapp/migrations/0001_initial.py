# Generated by Django 4.1.5 on 2023-02-23 03:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messier', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('type', models.CharField(max_length=50)),
                ('ar', models.CharField(max_length=50)),
                ('dec', models.CharField(max_length=50)),
                ('dist', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='album/images')),
            ],
            options={
                'verbose_name_plural': 'Objetos Messier',
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('swap_status', models.BooleanField(default=False)),
                ('catalogue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albumapp.catalogue')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
