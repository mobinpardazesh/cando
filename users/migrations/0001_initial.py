# Generated by Django 4.0 on 2023-08-19 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_familly', models.CharField(max_length=100)),
                ('user_age', models.IntegerField(default=0)),
                ('user_fathername', models.CharField(max_length=100)),
                ('user_username', models.CharField(max_length=100)),
                ('user_password', models.CharField(default='123', max_length=100)),
                ('user_email', models.EmailField(max_length=100)),
            ],
        ),
    ]
