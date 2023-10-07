from django.db import models
from django.urls import reverse
# Create your models here.
class Catagory(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    Description = models.TextField(blank=True)
    Image = models.ImageField(upload_to='Catagory',blank=True)


    class Meta:
        ordering=('name',)
        verbose_name='Catagory'
        verbose_name_plural='Catagories'

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('ecommerce_app:product_by_catagory',args=[self.slug])

class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    Description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='Product', blank=True)
    stock = models.IntegerField()
    availability = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


    def __str__(self):
            return '{}'.format(self.name)

    def get_url(self):
        return reverse('ecommerce_app:ProCatDetail',args=[self.catagory.slug, self.slug])

