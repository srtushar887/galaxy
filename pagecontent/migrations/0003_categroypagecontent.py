# Generated by Django 3.0.2 on 2020-01-18 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20200117_1153'),
        ('pagecontent', '0002_homeslider'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategroyPageContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=200)),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='category.Subcategory')),
            ],
        ),
    ]
