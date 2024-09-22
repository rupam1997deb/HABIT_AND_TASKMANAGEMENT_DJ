from django.db import models

class DailyHabitLog(models.Model):
    date = models.DateField()
    wakeup_time = models.CharField(max_length=10)
    gratitude_written = models.CharField(max_length=10)
    workout_done = models.CharField(max_length=10)
    book_reading_done = models.CharField(max_length=10)
    python_problems_solved = models.CharField(max_length=10)
    python_advanced = models.CharField(max_length=10)
    asleep_by_midnight = models.CharField(max_length=10)

    def __str__(self):
        return f'Daily Habit Log - {self.date}'


class DailyTask(models.Model):
    CATEGORY_CHOICES = (
        ('O', 'Officw'),
        ('P', 'Personal')
        )
    date = models.DateField()
    task_name = models.CharField(max_length=200)
    status = models.TextField()
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    roadblocks = models.TextField(blank=True, null=True)

    def __Str__(self):
        return f"{self.task_name} - {self.date}"

