# Generated by Django 3.0.2 on 2020-01-18 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagecontent', '0006_auto_20200118_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalsetting',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='generalsetting',
            name='phone_number',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
