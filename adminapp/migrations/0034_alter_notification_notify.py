# Generated by Django 3.2.5 on 2021-11-02 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0033_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notify',
            field=models.CharField(max_length=500),
        ),
    ]
