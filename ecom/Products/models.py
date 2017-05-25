#from django.core.urlresolvers import reverse
from django.db import models
# Create your models here.


class Product(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(null=True, blank=True)
	price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)

	def __unicode__(self):
		return self.title

	def get_price(self):
		return self.price

#	def get_absolute_url(self):
#		return reverse("single_product", kwargs={"slug": self.slug})


class ProductImage(models.Model):
	product = models.ForeignKey(Product)
	image = models.ImageField(upload_to='products/images/')

	def __unicode__(self):
		return self.product.title
