# Generated by Django 4.0.4 on 2022-06-10 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userinterest_userprofile_interests'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
    ]
