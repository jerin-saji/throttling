from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.name
