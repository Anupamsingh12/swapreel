# Generated by Django 3.1.2 on 2021-05-20 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0015_post_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]
