# Generated by Django 3.2.5 on 2021-10-19 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminapp', '0022_auto_20211019_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cf', models.CharField(max_length=30)),
                ('ca', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=40)),
                ('doc', models.DateField()),
                ('description', models.CharField(max_length=100)),
            ],
        ),
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
            name='employeedetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('middlename', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('fathersname', models.CharField(max_length=30)),
                ('maritalstatus', models.CharField(max_length=30)),
                ('employeetype', models.CharField(max_length=30)),
                ('doj', models.DateField()),
                ('employeegrade', models.CharField(max_length=30)),
                ('shift', models.CharField(max_length=30)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.department')),
                ('designation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.designation')),
            ],
        ),
        migrations.CreateModel(
            name='leavetype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leavetype', models.CharField(max_length=40)),
            ],
        ),
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
        migrations.CreateModel(
            name='officialdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='adminapp.employeedetail')),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.employeedetail')),
            ],
        ),
        migrations.CreateModel(
            name='document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate', models.CharField(max_length=100)),
                ('resume', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=100)),
                ('personal_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='adminapp.employeedetail')),
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
                ('personal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.employeedetail')),
            ],
        ),
    ]
