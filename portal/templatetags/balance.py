from django import template
import locale
locale.setlocale(locale.LC_ALL, '')
#locale.setlocale(locale.LC_ALL, 'en_CA.UTF-8' )

register = template.Library()
 
 
@register.filter()
def currency(value):
    return locale.currency(float(value),symbol=False, grouping=True)


@register.filter(name="get_balance")
def get_balance():
    balance = 0
    return balance

@register.filter(name="set_balance")
def set_balance(balance, amount):
    balance = float(amount)
    return balance



@register.filter(name="add_to_balance")
def add_to_balance(balance, amount):
    return balance + float(amount)

@register.filter(name="subtract_from_balance")
def subtract_from_balance(balance, amount):
    return float(balance) - float(amount)