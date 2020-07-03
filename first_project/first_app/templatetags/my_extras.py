from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    this cuts all value of arg from the string
    """
    return value.replace(arg,'')

# register.filter('cut',cut)   # function name in the page and function nam ef filter created
