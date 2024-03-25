from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Catagories(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class FilterPrice(models.Model):
    FILTER_PRICE = (
        ('10-20', '10-20'),
        ('20-30', '20-30'),
        ('30-40', '30-40'),
        ('40-50', '40-50'),
    )
    price = models.CharField(choices=FILTER_PRICE, max_length=200)
    def __str__(self):
        return self.price

class Product(models.Model):
    CONDITION = (
        ('NEW', 'NEW'),
        ('OLD', 'OLD'),
    )
    STOCK = (
        ('INSTOCK', 'INSTOCK'),
        ('OUTSTOCK', 'OUTSTOCK'),
    )
    STATUS = (
        ('PUBLISHED', 'PUBLISHED'),
        ('DRAFT', 'DRAFT'),
    )
    Unique_Id = models.CharField(unique=True, max_length=200, null=False)
    image = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    Condition = models.CharField(choices=CONDITION, max_length=200)
    discription = models.TextField()
    stock = models.CharField(choices=STOCK, max_length=200)
    status = models.CharField(choices=STATUS, max_length=200)
    catagory = models.ForeignKey(Catagories, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    filterprice = models.ForeignKey(FilterPrice, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=200)
    message=models.TextField(max_length=200)
    def __str__(self) :
        return self.name

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    address=models.TextField()
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=200)
    postcode=models.IntegerField()
    phonenumber=models.IntegerField()
    email=models.EmailField()
    ammount=models.CharField(max_length=200)
    payment_id=models.CharField(max_length=200,null=True,blank=True)
    paid=models.BooleanField(default=False,null=True)
    def __str__(self) :
        return self.user

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.CharField(max_length=200)
    image=models.ImageField(upload_to='pictures')
    quantity=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    total=models.CharField(max_length=200)
    def __str__(self) :
        return self.order