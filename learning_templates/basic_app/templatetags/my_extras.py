from django import template
register = template.Library()

#@register.filter(name='cutout')
@register.filter
def cutout(value, arg):
    return value.replace(arg, '')
#register.filter('cutout',cutout)
