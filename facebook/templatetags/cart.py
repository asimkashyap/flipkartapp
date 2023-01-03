from ..models import Product
from django import template

register = template.Library()


@register.filter(name="isexistincart")
def isexistincart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False


@register.filter(name="cartquantity")
def cartquantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return False


@register.filter(name="Total_price")
def Total_price(product, cart):
    tp = product.price * cartquantity(product, cart)
    return tp


@register.filter(name="payable_amount")
def payable_amount(product, cart):
    s = 0
    for i in product:
        s = s + Total_price(i, cart)
    return s


@register.filter(name="prod_price")
def prod_price(price, quantity):
    tp = price * quantity
    return tp
