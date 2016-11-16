from django_jinja import library

from ..models import Partner


@library.global_function
def get_partners():
    return Partner.objects.all()
