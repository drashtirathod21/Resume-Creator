# Generated by Django 3.2.4 on 2021-07-02 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeApp', '0002_alter_user_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ProfilePic',
            field=models.FileField(default='default.png', upload_to='users/'),
        ),
    ]
