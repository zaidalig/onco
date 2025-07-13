from django import template
from accounts.views import get_user_role

register = template.Library()

@register.simple_tag
def user_role(user):
    return get_user_role(user)
