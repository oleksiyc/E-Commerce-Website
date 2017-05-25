
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from ecom.models import User, Item, Basket, BasketItem
from django.core import serializers

appname = 'ecom'

def loggedin(f):
    def test(request):
        if 'username' in request.session:
            return f(request)
        else:
            return render(request, 'ecom/loginpage.html', {})
    return test

def index(request):
    if loggedin():
        return render(request, 'ecom/main.html')
    else:
        return render(request, 'ecom/loginpage.html')

def basket(request):
    return render(request, 'ecom/basket.html')

def signup(request):
    return render(request, 'ecom/signup.html',)

def loginpage(request):
    return render(request, 'ecom/loginpage.html')

def main(request):
    return render(request, 'ecom/main.html')

#@loggedin
def myaccount(request):
    pk = request.session['username']
    user = User.objects.get(pk=pk)
    context = {
	"fname": user.firstname,
        "uname": user.username,
        "email": user.email,
        "address": user.address,
        "city": user.city,
        "postcode": user.postcode,
        'loggedin': True
    }
    return render(request, 'ecom/myaccount.html', context)

def changeQuantity(request):
    username = request.session['username']
    user = User.objects.get(pk=username)
    basket = user.basket
    basketItems = basket.basketitem_set.all()
    for x in basketItems:
        article_id = request.GET.get('article_id')
        if x.product.article_id == article_id:
            x.quantity = x.quantity + int(request.GET.get('value'))
            x.save()
    return HttpResponse(200)

def getProductsInbasket(request):
    username = request.session['username']
    user = User.objects.get(pk=username)
    basket = user.basket

    basketItems = basket.basketitem_set.all()
    products = []

    for x in basketItems:
        products.append(x.product)

    data = serializers.serialize("json", products)
    return HttpResponse(data)

def getProducts(request):
	data = serializers.serialize("json", Item.objects.all())
	return HttpResponse(data)

def buyProduct(request):
    username = request.session['username']
    user = User.objects.get(pk=username)
    pk = request.GET.get("article_id")
    item = Item.objects.get(pk=pk)
    item.sold = True

    basketItem = BasketItem(basket=user.basket, product=item)
    basketItem.save()
    item.save()
    user.save()
    subject = 'Thank you for your purchase'
    message = 'This is confirmation your order has been placed'
    from_email = setting.EMAIL_HOST_USER
    to_list = [user.email, settings.EMAIL_HOST_USER]
    send_mail(subject, message, from_email, to_list, fail_silently = True)
    return HttpResponse(200)


def register(request):
    u = request.POST.get('username')
    fname = request.POST.get('fname')
    sname = request.POST.get('sname')
    date = request.POST.get('dob')
    phonenum = request.POST.get('phonenum')
    email = request.POST.get('email')
    address = request.POST.get('address')
    city = request.POST.get('city')
    postcode = request.POST.get('postcode')
    p = request.POST.get('password')
    basket = Basket()
    basket.save()
    user = User(username=u,
                 firstname=fname,
                 surname=sname,
                 dob=date,
                 phone=phonenum,
                 email=email,
                 address=address,
                 city=city,
                 postcode=postcode,
                 password=p,
                 basket= basket
                 )
    user.save()
    return render(request, 'ecom/loginpage.html')


def login(request):
    if 'username' not in request.GET:
        context = {
            'errorText': "Please enter a username"
         }
        return render(request, 'ecom/loginpage.html', context)
    else:
        usrn = request.GET['username']
        pwd = request.GET['password']
        try:
            user = User.objects.get(pk=usrn)
        except User.DoesNotExist:
            context = {
                'errorText': "The username you entered does not exist"
            }
            return render(request, 'ecom/loginpage.html', context)
        if pwd == user.password:
            request.session['username'] = usrn;
            request.session['password'] = pwd;
            request.session['basket'] = None;
            return render(request, 'ecom/main.html', {
                'appname': appname,
                'username': usrn,
                'loggedin': True}
            )
        else:
            context = {
                'errorText': "Incorrect password"
            }
            return render(request, 'ecom/loginpage.html', context)

#@loggedin
def logout(request):
    if 'username' in request.session:
        request.session.flush()
        return render(request, 'ecom/loginpage.html')
    else:
        raise Http404("Can't logout, you are not logged in")

