import datetime
from django import template

register = template.Library()

@register.filter
def unix_to_date(unix_str):
    try:
        unix_int = int(unix_str)
    except (ValueError, TypeError):
        return 'error converting'
    
    if not isinstance(unix_int, (int, float)):
        return 'NOT UNIX'
    return datetime.datetime.fromtimestamp(unix_int).strftime('%d/%m/%Y')