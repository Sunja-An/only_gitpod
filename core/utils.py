import jwt
import json
import requests

from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from my_settings import SECRET_KEY
from myapp.models import Account

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization', None)
            payload = jwt.decode(access_token, SECRET_KEY, algorithms='HS256')
            user = Account.objects.get(email=payload['email'])
            request.user = user
        
        except jwt.exceptions.DecodeError:
            return JsonResponse({'message': 'INVALID_KEY'}, status=400)
        
        except Account.DoesNotExist:
            return JsonResponse({'message': 'INVALID_KEY'}, status=400)

        return func(self, request, *args, **kwargs)
    return wrapper