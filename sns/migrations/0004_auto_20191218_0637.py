# Generated by Django 2.2.8 on 2019-12-18 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sns', '0003_auto_20191218_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_who', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friend',
            name='whom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_whom', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Friend_request_who', to=settings.AUTH_USER_MODEL)),
                ('whom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Friend_request_whom', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('who', 'whom')},
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Follow_who', to=settings.AUTH_USER_MODEL)),
                ('whom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Follow_whom', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('who', 'whom')},
            },
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Block_who', to=settings.AUTH_USER_MODEL)),
                ('whom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Block_whom', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('who', 'whom')},
            },
        ),
    ]