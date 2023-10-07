from django.shortcuts import render, redirect, get_object_or_404
from ecommerce_app.models import Product,Catagory
from .models import Cart,CartItems
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def cartId(request):
    cart = request.session.session_key
    if not cart:
        cart= request.session.create()

    return cart

def addCart(request,product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cartId=cartId(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cartId=cartId(request)
        )
        cart.save()

    try:
        cart_items = CartItems.objects.get(product=product,cart=cart)
        if cart_items.quantity < cart_items.product.stock:
            cart_items.quantity += 1
        cart_items.quantity +=1
        cart_items.save()
    except CartItems.DoesNotExist:
        cart_items=CartItems.objects.create(product=product,quantity=1,cart=cart)
        cart_items.save()

    return redirect('CartApp:cartDetail')

def cartDetail(request,total=0,counter=0,cart_items=None):
    try:
        cart=Cart.objects.get(cartId=cartId(request))
        cart_items=CartItems.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter +=cart_item.quantity

    except ObjectDoesNotExist:
        pass

    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))

def cartRemove(request,product_id):
    cart = Cart.objects.get(cartId=cartId(request))
    product = get_object_or_404(Product,id=product_id)
    cart_item = CartItems.objects.get(product=product,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('CartApp:cartDetail')

def fullRemove(request,product_id):
    cart = Cart.objects.get(cartId=cartId(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItems.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('CartApp:cartDetail')