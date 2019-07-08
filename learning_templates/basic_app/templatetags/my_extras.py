from django import template

register = template.Library()

# Alternative method of registering our filters
@register.filter(name='cut')
def cut(value, arg):
    """
    This func cuts out all values of "arg" from the string
    """
    return value.replace(arg,'')

# we the finally register this new custom filter
# register.filter('cut', cut)
