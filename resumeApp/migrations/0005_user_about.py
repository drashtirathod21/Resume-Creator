# Generated by Django 3.2.4 on 2021-07-07 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeApp', '0004_alter_user_profilepic'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='About',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
