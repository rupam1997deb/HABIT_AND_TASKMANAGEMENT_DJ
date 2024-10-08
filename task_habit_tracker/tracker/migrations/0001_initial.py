# Generated by Django 5.1.1 on 2024-09-22 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyHabitLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('wakeup_time', models.CharField(max_length=10)),
                ('gratitude_written', models.CharField(max_length=10)),
                ('workout_done', models.CharField(max_length=10)),
                ('book_reading_done', models.CharField(max_length=10)),
                ('python_problems_solved', models.CharField(max_length=10)),
                ('python_advanced', models.CharField(max_length=10)),
                ('asleep_by_midnight', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DailyTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('task_name', models.CharField(max_length=200)),
                ('status', models.TextField()),
                ('category', models.CharField(choices=[('O', 'Officw'), ('P', 'Personal')], max_length=2)),
                ('roadblocks', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
