from .models import get_info


def add_info(request):
    info = get_info()
    return {'info': info}
