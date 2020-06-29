from cgi import parse_qs
from template import html


def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', ['0'])[0]
    b = d.get('b', ['0'])[0]
    try:
        a, b = int(a), int(b)
        x = a + b
        y = a * b
    except ValueError:
        x = -1
        y = -1
    response_body = html%{
            'sum':x,
            'mul':y,
    }

    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
