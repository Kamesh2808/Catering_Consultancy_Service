# Generated by Django 5.1.1 on 2024-10-08 06:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sign_up_cater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Uname', models.CharField(max_length=20)),
                ('Mailid', models.CharField(max_length=20)),
                ('Phone', models.CharField(max_length=20)),
                ('Pass', models.CharField(max_length=20)),
                ('Cpass', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='sign_up',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Uname', models.CharField(max_length=20)),
                ('Mailid', models.CharField(max_length=20)),
                ('Phone', models.CharField(max_length=20)),
                ('Pass', models.CharField(max_length=20)),
                ('Cpass', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='catering_info',
            fields=[
                ('Cname', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('Menu', models.CharField(max_length=100)),
                ('Cuisine', models.CharField(max_length=100)),
                ('Availability', models.CharField(max_length=100)),
                ('Experience', models.CharField(max_length=100)),
                ('Additionalservices', models.CharField(max_length=100)),
                ('About', models.CharField(max_length=1000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Home.sign_up_cater')),
            ],
        ),
    ]