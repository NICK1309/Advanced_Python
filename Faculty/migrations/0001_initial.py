# Generated by Django 4.2 on 2023-04-16 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacherName', models.CharField(max_length=200)),
                ('teacherSubject', models.CharField(max_length=200)),
                ('teacherCollegeName', models.CharField(max_length=200)),
            ],
        ),
    ]