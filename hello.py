def hello(environ, start_response):
  status = '200 OK'
  headers = [
    ('Content-Type', 'text/plain')
  ]

  query = environ.QUERY_STRING.split('&');
  result = '\n'.join(query)
  start_response(status, headers)
  return [result]