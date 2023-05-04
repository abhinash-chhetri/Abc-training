# Generated by Django 4.2.1 on 2023-05-04 11:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(limit_value=10)])),
                ('qualifications', models.CharField(max_length=30)),
                ('experience', models.PositiveSmallIntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Instructors',
                'db_table': 'Instructor',
            },
        ),
        migrations.CreateModel(
            name='Upcomingclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('duration', models.CharField(max_length=25)),
                ('price', models.PositiveIntegerField()),
                ('start_date', models.DateField()),
                ('time', models.CharField(max_length=10)),
                ('Instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='training_app.instructor')),
            ],
            options={
                'verbose_name_plural': 'Upcomingclasses',
                'db_table': 'Upcomingclass',
            },
        ),
    ]