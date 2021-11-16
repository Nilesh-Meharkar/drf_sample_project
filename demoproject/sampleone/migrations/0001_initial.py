# Generated by Django 3.2.9 on 2021-11-16 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
            ],
        ),
    ]