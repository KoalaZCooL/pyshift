#!/usr/bin/env python
import os
import json
try:
    # for Python3
    import urllib.parse as urlparse
except ImportError:
    # for Python2
    import urlparse

def application(environ, start_response):

    ctype = 'application/json'
    query_parsed = urlparse.parse_qs(environ['QUERY_STRING'])

    if environ['PATH_INFO'] == '/api/token':
        #af29ff93-3045-4c72-ae27-12480fdeb7bf
        response_body = 'Z'
    elif environ['PATH_INFO'] == '/api/reversewords':
        word_reverse = []
        original = query_parsed.get('sentence')[0].split(' ')

        for s in original:
            word_reverse.append(s[::-1])

        response_body = json.dumps(' '.join(word_reverse))

    elif environ['PATH_INFO'] == '/api/fibonacci':
        response_body = json.dumps(' '.join([]))
    elif environ['PATH_INFO'] == '/api/triangletype':
        response_body = 'triangletype'
    elif environ['PATH_INFO'] == '/env':
        response_body = ['%s: %s' % (key, value)
                    for key, value in sorted(environ.items())]
        response_body = '\n'.join(response_body)
    else:
        response_body = '''Hello World'''
    # response_body = response_body.encode('utf-8')

    status = '200 OK'
    response_headers = [('Content-Type', ctype), ('Content-Length', str(len(response_body)))]
    #
    start_response(status, response_headers)
    return [response_body ]

#
# Below for testing only
#
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8051, application)
    # Wait for a single request, serve it and quit.
    httpd.handle_request()
