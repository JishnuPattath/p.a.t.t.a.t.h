from .models import Cart, CartItems
from .views import cartId

def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cartId=cartId(request))
            cart_items = CartItems.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                item_count += cart_item.quantity

        except Cart.DoesNotExist:
            item_count = 0

    return dict(item_count=item_count)