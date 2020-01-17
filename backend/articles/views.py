from . import models
import django.http
import json

model = models.Article

def getall(request : django.http.request.HttpRequest):
    objs = model.objects.all()
    many = []
    for o in objs:
        many.append(o.toDict())
    js = {'response' : many}
    return django.http.JsonResponse(js)

def getone(request : django.http.request.HttpRequest):
    print('here me')
    oid = request.GET['id']
    single = model.objects.get(id=oid)
    single = single.toDict()
    js = {'response' : single}
    return django.http.JsonResponse(js)
