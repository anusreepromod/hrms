# Generated by Django 3.2.5 on 2021-10-06 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0019_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mtitle', models.CharField(max_length=40)),
                ('mdate', models.CharField(max_length=40)),
                ('mtime', models.CharField(max_length=40)),
                ('agenda', models.CharField(max_length=60)),
            ],
        ),
    ]
