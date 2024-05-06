import time


def log_request(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Хотим что то сделать с запросом

        print('GET REQUEST')
        print(request)
        print('END')

        print('IS GET', request.is_get)
        print('IS POST', request.is_post)

        response = get_response(request)

        # Хотим что то сделать с ответом
        print('GET RESPONSE')
        print(response)
        print('END')

        return response

    return middleware


class TimeDebugMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        start_time = time.time()

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        end_time = time.time()

        delta_time = end_time - start_time

        print('RESPONSE TIME:', delta_time)

        return response


def beauty_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Хотим что то сделать с запросом
        request.is_get = request.method == 'GET'
        request.is_post = request.method == 'POST'

        response = get_response(request)

        return response

    return middleware


def ban_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Хотим что то сделать с запросом

        # request.ip - получаем ip

        # request counter (база реального времени)

        # if ip in base return 404
            # block

        response = get_response(request)

        return response

    return middleware
