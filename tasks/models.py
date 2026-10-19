from django.db import models

# Create your models here.
class Task(models.Model):
    PRIORITY_CHOICES = [("low", "LOW"), ("medium", "MEDIUM"), ("high", "HIGH")]
    STATUS_CHOICES = [("pending", "PENDING"), ("in_progress", "IN PROGRESS"), ("completed", "COMPLETED")]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="medium")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return self.title