# Generated by Django 3.1.3 on 2020-12-05 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20201205_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='/media/users/profile_pic_default.png', upload_to='users'),
        ),
    ]
