from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATE_CHOICES=(
    ('P1','Koshi'),
    ('P2','Madhesh'),
    ('P3','Bagmati'),
    ('P4','Gandaki'),
    ('P5','Lumbini'),
    ('P6','Karnali'),
    ('P7','Sudurpashchim'),
)
CATAGORY_CHOICES=(
    ('CR','Curd'),
    ('ML','Milk'),
    ('LS','Lassi'),
    ('MS','Milkshake'),
    ('PN','Paneer'),
    ('GH','Ghee'),
    ('CZ','Cheese'),
    ('IC','Ice-Creams'),
)
STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way','On the way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
)

class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.FloatField()
    razorpay_order_id=models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status=models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id=models.CharField(max_length=100,blank=True,null=True)
    paid=models.BooleanField(default=False)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description=models.TextField()
    composition = models.TextField(default="")
    prodapp = models.TextField(default="")
    category =models.CharField(choices=CATAGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
    
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField( choices = STATE_CHOICES, max_length=200)
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)