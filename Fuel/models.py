from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Login(AbstractUser):
    userType = models.CharField(max_length=100)
    viewPass = models.CharField(max_length=100, null=True)
    regDate = models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return self.username


class Shops(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100,null=True)
    phone = models.IntegerField(null=True)
    rnumber = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to="image",null=True)
    address = models.CharField(max_length=300,null=True)
    status = models.CharField(max_length=100,null=True)
    loginid = models.ForeignKey(Login, on_delete=models.CASCADE, default=1,null=True)

    def __str__(self):
        return self.name



class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=300)
    loginid = models.ForeignKey(Login, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="image",null=True)


    def __str__(self):
        return self.name
    

class Trainer(models.Model):
    name = models.CharField(max_length=100,null=True)
    age = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=100,null=True)
    phone = models.IntegerField(null=True)
    image = models.ImageField(upload_to="image",null=True)
    certificate = models.ImageField(upload_to="image",null=True)
    desc = models.CharField(max_length=300,null=True)
    qualification = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=200,null=True)
    loginid = models.ForeignKey(Login, on_delete=models.CASCADE, default=1,null=True)


class Products(models.Model):
    name = models.CharField(max_length=50,null=True)
    desc = models.CharField(max_length=200,null=True)
    age = models.CharField(max_length=50,default="Any Age")
    price = models.IntegerField(null=True)
    exptime = models.CharField(max_length=50,null=True)
    available=models.CharField(max_length=50,default="Not Available")
    status = models.CharField(max_length=50,default="Not Approved")
    image = models.ImageField(upload_to="image",null=True)
    company = models.CharField(max_length=50,null=True)
    sid = models.ForeignKey(Shops, on_delete=models.CASCADE)

class Booking(models.Model):
    uid=models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50,null=True)
    date=models.DateField(auto_now_add=True)
    tot=models.IntegerField(null=True)

class ChildBooking(models.Model):
    bid=models.ForeignKey(Booking, on_delete=models.CASCADE)
    pid = models.ForeignKey(Products, on_delete=models.CASCADE)
    count = models.IntegerField(null = True)
    tot = models.IntegerField(null=True)

class Cart(models.Model):
    uid=models.ForeignKey(User, on_delete=models.CASCADE)
    pid = models.ForeignKey(Products, on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)

class Articles(models.Model):
    heading = models.CharField(max_length=100,null=True)
    paragraph = models.CharField(max_length=200,null=True)
    image = models.ImageField(null=True)
    date = models.DateTimeField(auto_now_add=True)


class Chat(models.Model):
    time=models.TimeField(auto_now_add=True)
    date=models.DateTimeField(auto_now_add=True)
    tid=models.ForeignKey(Trainer, on_delete=models.CASCADE)
    uid=models.ForeignKey(User, on_delete=models.CASCADE)
    message=models.CharField(max_length=100,null=True)
    sender=models.CharField(max_length=100,null=True)


