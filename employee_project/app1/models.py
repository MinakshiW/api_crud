from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=34)
    email = models.EmailField()
    registered_time = models.DateTimeField(auto_now_add=True)
    registered_by = models.CharField(max_length=34)