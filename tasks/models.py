from django.db import models
from django.contrib.auth.models import User  # Import the User model for assigning tasks to users

class Task(models.Model):
    objects = None
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assign a task to a user
    title = models.CharField(max_length=255)  # Title of the task
    description = models.TextField(blank=True, null=True)  # Optional task description
    priority = models.IntegerField()  # Priority level (e.g., 1 = High, 2 = Medium, 3 = Low)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)  # Task status
    deadline = models.DateTimeField()  # Deadline for the task
    attachment = models.FileField(upload_to='uploads/', blank=True, null=True)  # Optional file attachment

    def __str__(self):
        return self.title

# Create your models here.
