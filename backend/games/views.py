from django.shortcuts import render
from . import models
import django.http
import json

model = models.Game

def getall(request : django.http.request.HttpRequest):
    objs = model.objects.all()
    many = []
    for o in objs:
        many.append(o.toDict())
    js = {'response' : many}
    return django.http.JsonResponse(js)

def getone(request : django.http.request.HttpRequest):
    oid = request.GET['id']
    single = model.objects.get(id=oid)
    single = single.toDict()
    js = {'response' : single}
    return django.http.JsonResponse(js)
