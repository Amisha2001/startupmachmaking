# Generated by Django 3.0.5 on 2021-04-25 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_job_opening'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_opening',
            name='comp_name',
        ),
    ]