# Generated by Django 3.0.5 on 2021-05-06 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20210506_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
