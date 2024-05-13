import json # imported this package to convert byte str to JSON: the byte str is the 'body = request.body' line
from django.forms.models import model_to_dict
from django.http import JsonResponse

from products.models import Product
# Create your views here.
def api_home(request, *args, **kwargs):
    #request -> HttpRequest -> Django
    #request.body is from the Django package
    # print(f"GET param test: {request.GET}") #url query params
    # print(f"POST param test: {request.POST}" )
    # body = request.body # JSON data in byte string which look like this on the cmd: b'{"query": "Hello world"}'
    #=====================converting byte str to JSON =========================================
    model_data = Product.objects.all().order_by("?").first()
    data = {} #<==converting the byte string to JSON AND STORING THE CONTENT INTO PYTHON DICT
    if model_data:
        data = model_to_dict(model_data, fields=['id','title', 'price']) #<<====You can now specify which fiend you want to extract here
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] =model_data.price 
        # model instance (model_data)
        # turn a Python dict
        # return JSON to my client

    # try: #<=======Try block in case Server does not contain Json data in which case it will return an empty dict
    #     data = json.loads(body) #<===this is the line that makes the conversion and stores the content into the empty list
    # except:
    #     pass
    # print(data) #<====This will print out the Json data after storing it in python dict 'data'
    # data['headers'] = dict(request.headers) #<====== You have to convert it into dict to get header informaton
    # data['params'] = dict(request.GET) #<===========
    # data['content_type'] = request.content_type
    # print (f" ====================================================: {request.content_type}")
    #===================================================================
    # print(body)#<==== body of request in byte str
    # return JsonResponse({"message": "Hello old friend"}) <===If uncommented it will just return hard code message
    return JsonResponse(data) #<========this will return the Jason response in python dict when requested by basic.py