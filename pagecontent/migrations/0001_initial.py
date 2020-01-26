# Generated by Django 3.0.2 on 2020-01-18 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='generalSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(max_length=100)),
                ('site_email', models.CharField(max_length=50)),
                ('site_logo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('site_icon', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
            ],
        ),
    ]