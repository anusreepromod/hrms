# Generated by Django 3.2.5 on 2021-11-09 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0034_alter_notification_notify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='leavecategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.leavetype'),
        ),
    ]