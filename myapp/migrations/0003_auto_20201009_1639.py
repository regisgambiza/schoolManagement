# Generated by Django 3.1.2 on 2020-10-09 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20201008_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learner',
            name='first_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.CreateModel(
            name='Pace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='', max_length=30)),
                ('pace_number', models.IntegerField(default=0)),
                ('date_issued', models.DateField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
                ('learner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='myapp.learner')),
            ],
        ),
    ]
