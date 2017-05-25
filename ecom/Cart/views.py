from django.shortcuts import render, HttpResponseRedirect

# Create your views here.

from Products.models import Product

from .models import Cart, CartItem

def view(request):
	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
	except:
		the_id = None
		
	if the_id:
		new_total = 0.00
		for item in cart.cartitem_set.all():
			line_total = float(item.product.price) * item.quantity
			new_total += line_total
		request.session['items_total'] = cart.cartitem_set.count()
		cart.total = new_total
		cart.save()
		context = {"cart": cart}
	else:
		empty_message = "Your Cart is Empty, please keep shopping."
		context = {"empty": True, "empty_message": empty_message}
	

	return render(request, 'cart.html', context)
