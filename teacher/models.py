from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name