# Generated by Django 3.2.5 on 2021-10-30 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0031_promotion_resignation'),
    ]

    operations = [
        migrations.CreateModel(
            name='leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeename', models.CharField(max_length=50)),
                ('leavecategory', models.CharField(max_length=40)),
                ('startdate', models.CharField(max_length=40)),
                ('enddate', models.CharField(max_length=40)),
                ('reason', models.CharField(max_length=40)),
                ('remark', models.CharField(max_length=40)),
                ('employeeid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.employeedetail')),
            ],
        ),
    ]
