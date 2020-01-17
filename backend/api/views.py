from django.contrib.auth import models, authenticate
from django import db
import django.http
import json
from django.views.decorators.csrf import csrf_exempt

model = models.User

#@csrf_exempt
def adduser(request : django.http.HttpRequest):
    params = request.POST
    print(params)
    login = params['login']
    email = params['email']
    password = params['password']
    try:
        user = model.objects.create_user(login, email, password)
        return django.http.JsonResponse({'response' : 'ok', 'user' : user.__str__()})
    except db.IntegrityError as err:
        print("hr")
        print(err.args)
        return django.http.JsonResponse({'response' : err.__str__()})
    except db.DataError as err:
        print("here")
        print(err.args)
        return django.http.JsonResponse({'response' : err.__str__()})
    except Exception as err:
        print(err)
        return django.http.JsonResponse({'response' : err.__str__()})


def getuser(request : django.http.HttpRequest):
    params = request.POST
    print(params)
    login = params['login']
    password = params['password']
    try:
        user = authenticate(request, username=login, password=password)
        if user is not None:
            return django.http.JsonResponse({'response' : 'ok', 'user' : user.__str__()})
        else:
            return django.http.JsonResponse({'response' : 'authentic err'})
    except Exception as err:
        print(err)
        return django.http.JsonResponse({'response' : err.__str__()})

def save(request : django.http.request.HttpRequest):
    args = request.GET.dict()
    print(args['game'])
    print(args['score'])
    js = {'response' : 'ok'}
    return django.http.JsonResponse(js)