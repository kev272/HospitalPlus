from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
class Doctors(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    message = models.TextField()
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Staff(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    hire_date = models.DateField()

    def __str__(self):
        return self.first_name + " " + self.last_name

class Ward(models.Model):
    name = models.CharField(max_length=50)
    totalbeds = models.IntegerField()
    availablebeds = models.IntegerField()

    def __str__(self):
        return self.name
class Medicine(models.Model):
    name = models.CharField(max_length=50)
    Treatment = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    date = models.DateTimeField()
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
    #mpesa api
class Transaction(models.Model):
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=[('Success', 'Success'), ('Failed', 'Failed')])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.amount} - {self.status}"