from models import *


def render_category(fn):
    def wrapper(request, *args,**kwargs):
        main_category = MainCategory.objects.all()
        return fn(request,main_category)
    return wrapper