# Generated by Django 5.0.4 on 2024-05-09 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(db_index=True, error_messages={'unique': 'User with this email already exists.'}, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(db_index=True, error_messages={'unique': 'User with this username already exists.'}, max_length=255, unique=True),
        ),
    ]