from django import template

register = template.Library()

@register.filter
def has_nota(inscripcion):
    return hasattr(inscripcion, 'nota')
