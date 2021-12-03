from django import template
from django.contrib.auth.models import Group 
from django.contrib.auth.decorators import user_passes_test

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name): 
    group = Group.objects.get(name=group_name) 
    return True if group in user.groups.all() else False

def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""

    Group.objects.get_or_create(name='seller-buyer')
    Group.objects.get_or_create(name='auctioneer')  
    Group.objects.get_or_create(name='admin')  

    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups)