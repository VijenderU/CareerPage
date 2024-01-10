# Generated by Django 5.0.1 on 2024-01-08 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('job_exp_years', models.DecimalField(decimal_places=2, max_digits=10)),
                ('salary', models.IntegerField(max_length=100)),
                ('emp_type', models.CharField(max_length=100)),
                ('job_location', models.CharField(max_length=100)),
                ('job_discription', models.CharField(max_length=100)),
                ('job_skills', models.CharField(max_length=100)),
            ],
        ),
    ]
