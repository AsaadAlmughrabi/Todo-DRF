from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False)
    user =  models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    genre= models.CharField(max_length=120, null=False, blank=False)
    
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
