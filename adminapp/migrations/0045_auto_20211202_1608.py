# Generated by Django 3.2.5 on 2021-12-02 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0044_contactdetails_document_employeedetail_leave_login_promotion_resignation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='personal_id',
        ),
        migrations.RemoveField(
            model_name='employeedetail',
            name='department_id',
        ),
        migrations.RemoveField(
            model_name='employeedetail',
            name='designation_id',
        ),
        migrations.RemoveField(
            model_name='leave',
            name='employeeid',
        ),
        migrations.RemoveField(
            model_name='leave',
            name='leavecategory',
        ),
        migrations.RemoveField(
            model_name='login',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='promotion',
            name='employeeid',
        ),
        migrations.RemoveField(
            model_name='resignation',
            name='employeeid',
        ),
        migrations.DeleteModel(
            name='contactdetails',
        ),
        migrations.DeleteModel(
            name='document',
        ),
        migrations.DeleteModel(
            name='employeedetail',
        ),
        migrations.DeleteModel(
            name='leave',
        ),
        migrations.DeleteModel(
            name='login',
        ),
        migrations.DeleteModel(
            name='promotion',
        ),
        migrations.DeleteModel(
            name='resignation',
        ),
    ]
