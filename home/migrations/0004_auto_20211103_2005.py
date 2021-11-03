# Generated by Django 3.2.8 on 2021-11-03 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_branch_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='createdDate',
            new_name='created_Date',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='updateDate',
            new_name='updatedDate',
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email_teacher',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone_teacher',
            field=models.CharField(max_length=100),
        ),
    ]
