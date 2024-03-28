from django import template

register = template.Library()

@register.filter
def get_first_half(sentence):
    words = sentence.split()
    half_index = len(words) // 2
    first_half = ' '.join(words[:half_index])
    return first_half

@register.filter
def get_second_half(sentence):
    words = sentence.split()
    half_index = len(words) // 2
    second_half = ' '.join(words[half_index:])
    return second_half