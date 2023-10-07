from django.db import models
from ecommerce_app.models import Product

# Create your models here.
class Cart(models.Model):
    cartId = models.CharField(max_length=250,blank=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['date']

    def __str__(self):
        return '{}'.format(self.cartId)

class CartItems(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItems'

    def subTotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return '{}'.format(self.product)

