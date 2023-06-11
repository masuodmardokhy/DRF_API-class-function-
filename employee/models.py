from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.IntegerField()
    post = models.CharField(max_length=30)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class Student(models.CharField):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    std_number = models.IntegerField()

    TEACHER = (
        ("ahmadi","Ahmadi"),
        ("abdi", "Abdi"),
        ("bahrami", "Bahrami"),
    )
    teacher = models.CharField(max_length=7, choices=TEACHER)

