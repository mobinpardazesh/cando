# Generated by Django 4.0 on 2023-08-15 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='USERNAME_FIELD',
            field=models.CharField(default='user', max_length=100),
        ),
    ]
