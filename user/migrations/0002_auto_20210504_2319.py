# Generated by Django 3.0.5 on 2021-05-04 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='avatar',
            field=models.ImageField(null=True, upload_to='profile_image'),
        ),
    ]