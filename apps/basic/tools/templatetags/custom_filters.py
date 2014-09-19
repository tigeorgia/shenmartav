from django.template.base import Library
from django.template.defaultfilters import stringfilter

register = Library()

@register.filter
@stringfilter
def shorten_text(value, max_length):
    if len(value) > max_length:
        shortened_val = value[:max_length]
        shortened_val = shortened_val[:shortened_val.rfind(" ")] + "..."
        return shortened_val
    return value

