from django.db import models

class Note(models.Model):
    COLOR_CHOICES = [
        ('light cloud', 'Light Cloud'),
        ('sunny yellow', 'Sunny Yellow'),
        ('mint green', 'Mint Green'),
        ('soft peach', 'Soft Peach'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    color = models.CharField(max_length=30, choices=COLOR_CHOICES, default='light cloud')

    def __str__(self):
        return self.title