from django.db import models
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    std_number = models.IntegerField()

    TEACHER = (
        ("ahmadi", "AHMADI"),
        ("abdi", "ABDI"),
        ("bahrami", "BAHRAMI"),
    )
    teacher = models.CharField(max_length=7, choices=TEACHER)
