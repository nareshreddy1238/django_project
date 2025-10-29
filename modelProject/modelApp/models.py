from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(unique=True)

class Programmer(models.Model):
    name = models.CharField(max_length=50)
    sal = models.IntegerField()

class Project(models.Model):
    name = models.CharField(max_length=100)
    programmers = models.ManyToManyField(Programmer)

class Customer(models.Model):
    name = models.CharField(max_length=20)

class PhoneNumber(models.Model):
    type = models.CharField(max_length=10)
    number = models.CharField(max_length=10)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)


class Person(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    age = models.IntegerField()

class License(models.Model):
    type = models.CharField(max_length=20)
    validFrom = models.DateField()
    validTo = models.DateField(null=True)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)