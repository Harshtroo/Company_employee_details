# Generated by Django 4.1.6 on 2023-02-13 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_alter_employee_depatments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='depatments',
            field=models.CharField(choices=[('CTO', 'CTO'), ('Developer', 'Developer'), ('HR', 'HR'), ('Admin', 'Admin')], max_length=10),
        ),
    ]