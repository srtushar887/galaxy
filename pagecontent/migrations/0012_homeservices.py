# Generated by Django 3.0.2 on 2020-01-26 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagecontent', '0011_homesectionone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homeservices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(blank=True, max_length=200)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]