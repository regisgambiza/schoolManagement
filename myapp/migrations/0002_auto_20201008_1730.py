# Generated by Django 3.1.2 on 2020-10-08 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='learner',
            name='grade',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='learner',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
