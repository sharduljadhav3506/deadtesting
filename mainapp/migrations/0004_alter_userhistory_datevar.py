# Generated by Django 4.2.13 on 2024-07-25 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_userhistory_image_alter_userhistory_datevar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userhistory',
            name='datevar',
            field=models.CharField(default='2024-07-25 21:04:30.955769', max_length=100),
        ),
    ]
