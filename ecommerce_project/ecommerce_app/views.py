from django.shortcuts import render, get_object_or_404
from .models import Product, Catagory
from django.core.paginator import Paginator,EmptyPage,InvalidPage


# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')


def allProduct_catagory(request, c_slug=None):
    c_page = None
    products_list = None
    if c_slug != None:
        c_page = get_object_or_404(Catagory, slug=c_slug)
        products_list = Product.objects.all().filter(catagory=c_page, availability=True)
    else:
        products_list = Product.objects.all().filter(availability=True)
    paginator = Paginator(products_list,6)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1

    try:
        products = paginator.page(page)
    except (EmptyPage,InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request, "catagory.html", {'catagory': c_page, 'products': products})

def ProDetail(request,c_slug,product_slug):
    try:
        product = Product.objects.get(catagory__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e

    return render(request,"product.html",{'product':product})