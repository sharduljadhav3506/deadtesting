# Generated by Django 4.2.13 on 2024-10-01 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0024_customuser_location_alter_userhistory_datevar'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='weight',
            field=models.TextField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='userhistory',
            name='datevar',
            field=models.CharField(default='2024-10-01 17:02:35.616013', max_length=100),
        ),
    ]
