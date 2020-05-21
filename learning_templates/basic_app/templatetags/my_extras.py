from django import template

register = template.Library()


@register.filter(name='cut_string')  # if name is left out it defaults to
# function name
def cut_string(value, arg):
    """this cuts out all values of "arg" from the string!"""

    return value.replace(arg, '')


# register.filter('cut_string', cut_string)
