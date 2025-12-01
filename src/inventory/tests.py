from django.test import TestCase

# Create your tests here.
request_get = {'page': 4, 'name': 'est', 'age_gte':25} # request.GET
# http://127.0.0.1/inventory/materials/?page=1&name=est&age_gte=25
print(request_get['page'])
request_get = {}
# http://127.0.0.1/inventory/materials/ --> http://127.0.0.1/inventory/materials/?page=2
# print(request_get['page'])
print(request_get.get('page', 1))

def f():
    ...

