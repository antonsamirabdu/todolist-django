from django.template import Library

register = Library()


@register.simple_tag
def my_simple_tag(user):
    return "{}".format(user)


@register.filter
def name_filter_cleaner(name):
    name_split = name.split('-')
    if len(name_split) > 1:
        result = f'{name_split[0]} {name_split[1]}'
    else:
        return name

    return result
