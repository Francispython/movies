# Generated by Django 4.1.2 on 2022-10-09 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='dfd', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
