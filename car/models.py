from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    data = models.DateTimeField(auto_now=True, auto_now_add=False)


class Car(models.Model):
    company = models.CharField(max_length=20)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


