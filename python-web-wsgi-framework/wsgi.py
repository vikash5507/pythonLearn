"""

https://testdriven.io/courses/python-web-framework/wsgi/

Our web framework will do something that no one is doing right now: 
IT WILL PRINT ALL ENVIRONMENT VARIABLES IT RECEIVES. Genius!
"""

from wsgiref.simple_server import make_server


class MiddleWare:
    def __init__(self, app):
        self.wrapped_app = app

    def __call__(self, environ, start_response, *args, **kwargs):
        wrapped_app_response = self.wrapped_app(environ, start_response)
        return [res[::-1] for res in wrapped_app_response]


def application(environ, start_response):
    response_body = [
        f'{key}: {value}' for key, value in sorted(environ.items())
    ]

    response_body = '\n'.join(response_body)
    status = '200 OK'

    response_headers = [
        ('Content-type', 'text/plain'),
    ]
    start_response(status, response_headers)

    return [response_body.encode('utf-8')]


def web_server():
    server = make_server('localhost', 8080, app=MiddleWare(application))
    server.serve_forever()


if __name__ == "__main__":
    web_server()
