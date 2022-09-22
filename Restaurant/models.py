from django.db import models


# Create your models here.
class User(models.Model):
    ROLE_CHOICES = {
        ('EMP', 'Employee'),
        ('CUS', 'Customer'),
    }
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phoneNumber = models.CharField(max_length=11, unique=True, editable=True)
    roles = models.CharField(max_length=3, choices=ROLE_CHOICES)

    def __str__(self):
        return self.email


class Address(models.Model):
    number = models.PositiveSmallIntegerField()
    street = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class FoodCategory(models.Model):
    category_name = models.CharField(max_length=255)
    food_item = models.ForeignKey('FoodItem', on_delete=models.PROTECT)


class FoodItem(models.Model):
    food_name = models.CharField(max_length=100)
    food_description = models.TextField(verbose_name='Text')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveSmallIntegerField()
    inventory = models.IntegerField()
    order = models.ForeignKey('Order', on_delete=models.PROTECT)


class Order(models.Model):
    order_number = models.IntegerField()
    order_time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    food_item = models.OneToOneField(FoodItem, on_delete=models.PROTECT, primary_key=True)
    quantity = models.PositiveSmallIntegerField()


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
