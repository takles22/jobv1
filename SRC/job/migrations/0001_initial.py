# Generated by Django 5.0.4 on 2024-04-10 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('job_type', models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=20)),
                ('Description', models.TextField(max_length=1000)),
                ('published_at', models.DateField(auto_now=True)),
                ('Vacancy', models.IntegerField(default=1)),
                ('salary', models.IntegerField(default=1000)),
                ('experience', models.IntegerField(default=1)),
            ],
        ),
    ]
