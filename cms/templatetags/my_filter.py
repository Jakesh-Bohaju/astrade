from django.template.defaultfilters import register


@register.filter(name='range')
def filter_range(start, end):
    return range(start, end)
