# Generated by Django 3.0.2 on 2020-01-26 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagecontent', '0012_homeservices'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homemiddlestatic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_title_one', models.CharField(blank=True, max_length=200)),
                ('first_title_two', models.CharField(blank=True, max_length=200)),
                ('first_background_image', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('first_number', models.CharField(blank=True, max_length=100)),
                ('second_title', models.CharField(blank=True, max_length=200)),
                ('second_description', models.TextField(blank=True)),
                ('second_image', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('second_youtube_url', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
