from django.shortcuts import render, Http404

# Create your views here.

from .models import Product, ProductImage

@loggedin
def search(request):
	try:
        q = request.GET.get('q') #parameter for the URL
	except:
		q = None
	
	if q:
		products = Product.objects.filter(title__icontains=q)
		context = {'query': q, 'products': products}
        return render(request, 'search.html', context)
	else:
		context = {}
	return render(request, 'products.html', context)

@loggedin
def all(request):
	products = Product.objects.all()
	context = {'products': products}
	return render(request, 'products.html', co@loggedinntext)

@loggedin
def single(request):
	try:
		product = Product.objects.all()
		images = product.productimage_set.all()
        		images = ProductImage.objects.filter(product=product)
        	context = {'product': product, "images": images
        		return render(request, 'products.html', context)
        	except:
		raise Http404
