from django import template

register = template.Library()

@register.filter(name='myLower')
def custLower(value):
    return value[:3].lower()

# register.filter('myLower', custLower)

@register.filter(name='myAppend')
def custAppend(value, arg):
    return str(arg)+value 