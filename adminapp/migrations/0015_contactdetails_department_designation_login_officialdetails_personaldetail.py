# Generated by Django 3.2.5 on 2021-10-01 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminapp', '0014_auto_20211001_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation_name', models.CharField(max_length=40)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.department')),
            ],
        ),
        migrations.CreateModel(
            name='personaldetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('middlename', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('fathersname', models.CharField(max_length=30)),
                ('maritalstatus', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='officialdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeetype', models.CharField(max_length=30)),
                ('doj', models.DateField()),
                ('employeegrade', models.CharField(max_length=30)),
                ('shift', models.CharField(max_length=30)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.department')),
                ('designation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.designation')),
                ('personal_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='adminapp.personaldetail')),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.personaldetail')),
            ],
        ),
        migrations.CreateModel(
            name='contactdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personalemail', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('pincode', models.IntegerField()),
                ('mobile', models.BigIntegerField()),
                ('personal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.personaldetail')),
            ],
        ),
    ]
