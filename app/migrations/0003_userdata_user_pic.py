# Generated by Django 3.1.1 on 2020-10-21 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_userdata_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='User_Pic',
            field=models.FileField(default='download.png', upload_to='profilepictures/'),
        ),
    ]