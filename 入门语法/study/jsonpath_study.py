import jsonpath

import json

obj =json.load(open('json/test.json', 'r', encoding='utf-8'))

# list =jsonpath.jsonpath(obj,'$..regionName')
list =jsonpath.jsonpath(obj,'$..A[(@.length-1)]')
print(list)