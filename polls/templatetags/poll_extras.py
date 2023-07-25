from django import template

register = template.Library()
#
#
#
@register.filter('comma_seprator')
def comma_seprator(value):
      
    return '{:,.0f}'.format(value)
    