# Generated by Django 5.0.6 on 2024-07-09 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=120)),
                ('file', models.FileField(upload_to='userfile')),
            ],
            options={
                'verbose_name': 'Signin',
                'verbose_name_plural': 'signin',
                'db_table': 'SIGNIN',
            },
        ),
    ]
