from django.conf.urls import url
from . import views

app_name = 'ecom'
urlpatterns = [
	# main page
    url(r'^$', views.index, name='index'),
    # signup page
    url(r'^signup/$', views.signup, name='signup'),
    # register
    url(r'^register/$', views.register, name='register'),
    # login page
    url(r'^login/$', views.login, name='login'),
    # login page
    url(r'^logout/$', views.logout, name='logout'),

    url(r'^getProducts/$', views.getProducts, name='getProducts'),

    url(r'^basket/$', views.basket, name='basket'),

    url(r'^getProductsInbasket/$', views.getProductsInbasket, name='getProductsInbasket'),

    url(r'^main/$', views.main, name='main'),

    url(r'^changeQuantity/$', views.changeQuantity, name='changeQuantity'),
    

    url(r'^buyProduct/$', views.buyProduct, name='buyProduct'),
    # login page
    url(r'^loginpage/$', views.login, name='loginpage'),
    # my account page
    url(r'^myaccount/$', views.myaccount, name='myaccount'),
]