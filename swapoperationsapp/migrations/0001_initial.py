# Generated by Django 4.1.5 on 2023-02-23 03:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('albumapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SwapOperations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emissor_album', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='emissor_album', to='albumapp.album')),
                ('emissor_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='emissor_user', to=settings.AUTH_USER_MODEL)),
                ('receptor_album', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='receptor_album', to='albumapp.album')),
                ('receptor_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='receptor_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]