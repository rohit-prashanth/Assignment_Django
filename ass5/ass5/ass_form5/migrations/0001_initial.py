# Generated by Django 3.2.5 on 2021-07-27 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScholoshipReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=10)),
                ('middlename', models.CharField(max_length=10)),
                ('lastname', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=10)),
                ('scholorship_catagory', models.CharField(max_length=10)),
                ('College', models.CharField(max_length=10)),
                ('aadhar_number', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_num', models.CharField(max_length=10)),
                ('address', models.TextField()),
            ],
        ),
    ]
