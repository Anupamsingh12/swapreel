# Generated by Django 3.1.2 on 2021-05-20 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0009_post_prof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='prof',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='manager.profile'),
        ),
    ]
