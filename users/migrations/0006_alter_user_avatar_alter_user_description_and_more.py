# Generated by Django 5.2 on 2025-04-14 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars'),
        ),
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=6),
        ),
    ]
