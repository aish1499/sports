# Generated by Django 3.0.2 on 2020-01-21 12:05

from django.db import migrations, models
import players.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100, verbose_name='user')),
                ('image', models.ImageField(upload_to=players.models.upload_image, verbose_name='Image')),
                ('message', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Message')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 's',
            },
        ),
    ]
