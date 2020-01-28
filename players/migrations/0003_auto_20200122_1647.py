# Generated by Django 3.0.2 on 2020-01-22 11:17

from django.db import migrations, models
import django.db.models.deletion
import players.models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20200121_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='players',
            name='message',
        ),
        migrations.RemoveField(
            model_name='players',
            name='user',
        ),
        migrations.AddField(
            model_name='players',
            name='caption',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='caption'),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=100, null=True, verbose_name='user')),
                ('image_2', models.ImageField(upload_to=players.models.upload_image, verbose_name='Image_2')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Message')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='players.Players', verbose_name='Post')),
            ],
        ),
    ]
