# Generated by Django 4.2.13 on 2024-07-25 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_category_item_userhistory_itemimage_useritem'),
    ]

    operations = [
        migrations.AddField(
            model_name='userhistory',
            name='image',
            field=models.ImageField(default='Error 404', max_length=300, upload_to='item_images/'),
        ),
        migrations.AlterField(
            model_name='userhistory',
            name='datevar',
            field=models.CharField(default='2024-07-25 20:34:36.675396', max_length=100),
        ),
    ]