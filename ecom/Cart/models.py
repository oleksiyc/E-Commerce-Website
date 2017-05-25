from django.db import models

# Create your models here.
from products.models import Product

class CartItem(models.Model):
	cart = models.ForeignKey('Cart', null=True, blank=True)
	product = models.ForeignKey(Product)
	quantity = models.IntegerField(default=1)
	line_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
	def __unicode__(self):
		try:
			return str(self.cart.id)
		except:
			return self.product.title


class Cart(models.Model):
	total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)

	def __unicode__(self):
		return "Cart id: %s" %(self.id)
