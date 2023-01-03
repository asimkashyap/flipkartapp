from .models import *
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework import routers, serializers, viewsets
from.serializers import UserSerializer


def index(request):

    if request.method == "POST":
        product_id = request.POST.get('cartid')
        remove = request.POST.get('minus')
        cart_id = request.session.get('cart')

        if cart_id:
            quantity = cart_id.get(product_id)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart_id.pop(product_id)
                    else:
                        cart_id[product_id] = quantity - 1
                else:
                    cart_id[product_id] = quantity + 1

            else:
                cart_id[product_id] = 1
        else:
            cart_id = {}
            cart_id[product_id] = 1
        request.session['cart'] = cart_id
        print(request.session['cart'])

    cate = Category.objects.all()
    cat_id = request.GET.get("category_id")
    if cat_id:
        pro = Product.objects.filter(category=cat_id)
    else:
        pro = Product.objects.all()
    return render(request, 'facebook.html', {'cat': cate, 'pro': pro})


def contact(request):

    return render(request, 'contact.html')


def user_registration(request):
    if request.method == "POST":
        f_name = request.POST.get('fname')
        l_name = request.POST.get('lname')
        email = request.POST.get('emailid')
        password = request.POST.get('pwd')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mbl')

        info = Signup(
            first_name=f_name,
            last_name=l_name,
            email=email,
            password=make_password(password),
            gender=gender,
            mobile=mobile)

        info.save()
        return render(request, 'facebook.html')


def Login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pwd')
        try:
            fetch_info = Signup.objects.get(email=email)
            if check_password(password, fetch_info.password):
                request.session['name'] = fetch_info.first_name
                request.session['customer'] = fetch_info.id
                return redirect('home')
            else:
                return HttpResponse("please enter valid password")
        except:
            return HttpResponse("enter the valid email")


def Logout(request):
    request.session.clear()
    return redirect('home')


def Cart(request):
    cart_info = request.session['cart'].keys()
    cart_dtls = Product.objects.filter(id__in=cart_info)
    return render(request, 'cart.html', {'cart_dtls': cart_dtls})


def Checkout(request):
    if request.method == "POST":
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        customer_id = request.session.get('customer')
        cart = request.session.get('cart')
        product = Product.objects.filter(id__in=list(cart.keys()))
        if not customer_id:
            return HttpResponse("please login")
        for pro in product:
            save_ord_dtls = Order(
                address=address,
                mobile_no=mobile,
                customer=Signup(id=customer_id),
                product=pro,
                quantity=cart.get(str(pro.id)),
                price=pro.price
            )
            save_ord_dtls.save()
        request.session['cart'] = {}
        return redirect('Order_dtls')


def Order_dtls(request):
    customer_id = request.session.get('customer')
    fetch_order = Order.objects.filter(customer=customer_id)
    tp = 0
    for i in fetch_order:
        print(i.quantity)
        tp = tp + (i.price * i.quantity)

    return render(request, 'order.html', {'fetch_order': fetch_order, 'tp': tp})

class UserViewSet(viewsets.ModelViewSet):
    queryset = Signup.objects.all()
    serializer_class = UserSerializer
