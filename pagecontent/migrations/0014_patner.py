# Generated by Django 3.0.2 on 2020-01-26 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagecontent', '0013_homemiddlestatic'),
    ]

    operations = [
        migrations.CreateModel(
            name='patner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
            ],
        ),
    ]
