from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class User(models.Model):
    user_id = models.CharField(max_length=10, unique=True)  # Set unique if it's an identifier
    user_name = models.CharField(max_length=255)  # Adjusted to CharField with a max length
    start_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Added updated_at for tracking modifications

    def __str__(self):
        return self.user_id